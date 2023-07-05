import astropy.wcs
import numpy as np
from astropy import units as u
from astropy.coordinates import (
    GCRS,
    ICRS,
    ITRS,
    CartesianRepresentation,
    EarthLocation,
    SkyCoord,
    solar_system_ephemeris,
)
from astropy.time import Time


class DistCalcHelper:
    """Helper class to hold the values needed to calculate the distance to an object.

    Parameters
    ----------

    distance : astropy.units.Quantity
        The distance from the barycenter to the position of interest in au
    obstime : astropy.time.Time
        The time of the observation
    helio : astropy.coordinates.ICRS
        The barycentric position of interest
    obs_pos_itrs : astropy.coordinates.ITRS
        The observer position in the ITRS frame.
    obs_pos : astropy.coordinates.ICRS
        The observer position in the barycentric frame at time t1.
        The vector from the barycenter to the observer at time t1.
    observer_to_object : astropy.coordinates.ICRS
        The vector from the observer at t1 to the position of interest in the ICRS frame.
        This is the ground truth as seen from the observer position at t1.
    cobs : astropy.coordinates.ICRS
        The unit vector (ra,dec) pointing to the position of interest as seen from the observer
        in the ICRS frame. This is the sky position that the observer
        would record as the line of sight of the position of interest
        and has no distance or time information.
    """

    def __init__(
        self, ra=90 * u.degree, dec=23.43952556 * u.degree, obstime="2023-03-20T16:00:00", distance=10 * u.au
    ) -> None:
        self.distance = distance
        self.obstime = Time(obstime, format="isot", scale="utc")
        self.helio = ICRS(ra, dec, distance=self.distance)
        self.obs_pos_itrs = None
        self.obs_pos = None
        self.observer_to_object = None
        self.cobs = None
        # todo: maybe use "jpl" in place of "de432s"?
        # todo: seems like the geocentric observer location (ctio) should be a parameter
        with solar_system_ephemeris.set("de432s"):
            self.obs_pos_itrs = EarthLocation.of_site("ctio").get_itrs(obstime=self.obstime)
            self.observer_to_object = ICRS(
                self.helio.transform_to(self.obs_pos_itrs).transform_to(GCRS(obstime=self.obstime)).cartesian
            )
            self.cobs = ICRS(ra=self.observer_to_object.ra, dec=self.observer_to_object.dec)
            self.obs_pos = ICRS(self.helio.cartesian - self.observer_to_object.cartesian)
            self.obs_pos = ICRS(CartesianRepresentation(self.obs_pos.cartesian.xyz.to(u.au)))

    def __repr__(self) -> str:
        ret = "\n".join(
            [
                f"distance={self.distance}",
                f"t1={self.obstime}",
                f"helio={self.helio}",
                f"obs_pos_itrs={self.obs_pos_itrs}",
                f"obs_pos={self.obs_pos}",
                f"observer_to_object={self.observer_to_object}",
                f"cobs={self.cobs}",
            ]
        )
        return ret
