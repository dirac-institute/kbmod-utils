import astropy.coordinates
import astropy.units
import pytest

from kbmod.utils.wcs import calc_actual_image_fov, construct_wcs_tangent_projection


def test_one_pixel():
    ref_val = astropy.coordinates.SkyCoord(ra=0 * astropy.units.deg, dec=0 * astropy.units.deg, frame="icrs")
    wcs = construct_wcs_tangent_projection(ref_val, img_shape=[1, 1], image_fov=3.5 * astropy.units.deg)
    assert wcs is not None
    skyval = wcs.pixel_to_world(0, 0)
    refsep = ref_val.separation(skyval).to(astropy.units.deg).value
    pytest.approx(refsep, 0.0001) == 0.0


def test_two_pixel():
    ref_val = astropy.coordinates.SkyCoord(ra=0 * astropy.units.deg, dec=0 * astropy.units.deg, frame="icrs")
    wcs = construct_wcs_tangent_projection(ref_val, img_shape=[2, 2], image_fov=3.5 * astropy.units.deg)
    assert wcs is not None
    skyval = wcs.pixel_to_world(0, 0)
    refsep = ref_val.separation(skyval).to(astropy.units.deg).value
    pytest.approx(refsep, 0.0001) == 0.0


def test_image_field_of_view():
    """Test that the image field of view can be set explicitly."""
    fov_wanted = 3.5 * astropy.units.deg
    ref_val = astropy.coordinates.SkyCoord(ra=0 * astropy.units.deg, dec=0 * astropy.units.deg, frame="icrs")
    wcs = construct_wcs_tangent_projection(
        ref_val, img_shape=[16, 16], image_fov=fov_wanted, solve_for_image_fov=True
    )
    assert wcs is not None
    fov_actual = calc_actual_image_fov(wcs)[0]
    pytest.approx(fov_actual.value, 1e-8) == fov_wanted.value


def test_image_field_of_view_wide():
    """Test that the image field of view measured
    off the image returned expected values.
    """
    fov_wanted = [30.0, 15.0] * astropy.units.deg
    ref_val = astropy.coordinates.SkyCoord(ra=0 * astropy.units.deg, dec=0 * astropy.units.deg, frame="icrs")
    wcs = construct_wcs_tangent_projection(
        ref_val, img_shape=[64, 32], image_fov=fov_wanted[0], solve_for_image_fov=True
    )
    assert wcs is not None
    fov_actual = calc_actual_image_fov(wcs)
    pytest.approx(fov_actual[0].value, 1e-8) == fov_wanted[0].value
    pytest.approx(fov_actual[1].value, 1e-8) == fov_wanted[1].value


def test_image_field_of_view_tall():
    """Test that the image field of view measured
    off the image returned expected values.
    """
    fov_wanted = [15.0, 29.05191311] * astropy.units.deg
    ref_val = astropy.coordinates.SkyCoord(ra=0 * astropy.units.deg, dec=0 * astropy.units.deg, frame="icrs")
    wcs = construct_wcs_tangent_projection(
        ref_val, img_shape=[32, 64], image_fov=fov_wanted[0], solve_for_image_fov=True
    )
    assert wcs is not None
    fov_actual = calc_actual_image_fov(wcs)
    pytest.approx(fov_actual[0].value, 1e-8) == fov_wanted[0].value
    pytest.approx(fov_actual[1].value, 1e-8) == fov_wanted[1].value
