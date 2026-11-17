
from pytest import approx
import pytest
import water_flow


def test_water_column_height():
    assert water_flow.water_column_height(0, 0) == approx(0)
    assert water_flow.water_column_height(0, 10) == approx(7.5)
    assert water_flow.water_column_height(25, 0) == approx(25)
    assert water_flow.water_column_height(48.3, 12.8) == approx(57.9)


def test_pressure_gain_from_water_height():
    assert water_flow.pressure_gain_from_water_height(0) == approx(0, abs=0.001)
    assert water_flow.pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert water_flow.pressure_gain_from_water_height(50) == approx(489.450, abs=0.001)


def test_pressure_loss_from_pipe():
    assert water_flow.pressure_loss_from_pipe(
        0.048692, 0, 0.018, 1.75) == approx(0, abs=0.001)

    assert water_flow.pressure_loss_from_pipe(
        0.048692, 200, 0, 1.75) == approx(0, abs=0.001)

    assert water_flow.pressure_loss_from_pipe(
        0.048692, 200, 0.018, 0) == approx(0, abs=0.001)

    assert water_flow.pressure_loss_from_pipe(
        0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001)

    # TODO: Add the remaining three pipe-loss test cases
    # using the values in your assignment table.


def test_pressure_loss_from_fittings():
    assert water_flow.pressure_loss_from_fittings(
        0, 3) == approx(0, abs=0.001)

    assert water_flow.pressure_loss_from_fittings(
        1.65, 0) == approx(0, abs=0.001)

    assert water_flow.pressure_loss_from_fittings(
        1.65, 2) == approx(-0.109, abs=0.001)

    # TODO: Add the remaining two fittings test cases.


def test_reynolds_number():
    assert water_flow.reynolds_number(
        0.048692, 0) == approx(0, abs=1)

    assert water_flow.reynolds_number(
        0.048692, 1.65) == approx(80069, abs=1)

    assert water_flow.reynolds_number(
        0.048692, 1.75) == approx(84922, abs=1)

    # TODO: Add the remaining two Reynolds number test cases.


def test_pressure_loss_from_pipe_reduction():
    reynolds = water_flow.reynolds_number(0.28687, 1.65)

    # TODO: Add all three pipe-reduction assertions.
    # Test velocities 0.00, 1.65, and 1.75.
    # Use the expected values from your assignment.


def test_kpa_to_psi():
    assert water_flow.kpa_to_psi(0) == approx(0)
    assert water_flow.kpa_to_psi(100) == approx(14.50377)


# Run pytest when this file is executed directly.
pytest.main(["-v", "--tb=line", "-rN", __file__])
