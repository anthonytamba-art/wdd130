
# Constants
PVC_SCHED80_INNER_DIAMETER = 0.28687
PVC_SCHED80_FRICTION_FACTOR = 0.013
SUPPLY_VELOCITY = 1.65

HDPE_SDR11_INNER_DIAMETER = 0.048692
HDPE_SDR11_FRICTION_FACTOR = 0.018
HOUSEHOLD_VELOCITY = 1.75

WATER_DENSITY = 998.2
GRAVITY = 9.80665
WATER_DYNAMIC_VISCOSITY = 0.0010016


def main():
    """Calculate and display water pressure at a house."""

    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90 degree angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    # Calculate water height and initial pressure
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    # Calculate pressure loss in the supply pipe
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY

    reynolds = reynolds_number(diameter, velocity)

    loss = pressure_loss_from_pipe(
        diameter, length1, friction, velocity)
    pressure += loss

    # Calculate pressure loss from fittings
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    # Calculate pressure loss from pipe reduction
    loss = pressure_loss_from_pipe_reduction(
        diameter,
        velocity,
        reynolds,
        HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    # Calculate pressure loss in the household pipe
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY

    loss = pressure_loss_from_pipe(
        diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


def water_column_height(tower_height, tank_height):
    """Calculate the height of the water column."""
    return tower_height + 3 * tank_height / 4


def pressure_gain_from_water_height(height):
    """Calculate pressure gain from water height."""
    return WATER_DENSITY * GRAVITY * height / 1000


def pressure_loss_from_pipe(
        pipe_diameter, pipe_length,
        friction_factor, fluid_velocity):
    """Calculate pressure loss through a pipe."""

    numerator = (
        -friction_factor
        * pipe_length
        * WATER_DENSITY
        * fluid_velocity ** 2)

    denominator = 2000 * pipe_diameter

    return numerator / denominator


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculate pressure loss from pipe fittings."""

    return (
        -0.04
        * WATER_DENSITY
        * fluid_velocity ** 2
        * quantity_fittings
        / 2000)


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculate the Reynolds number."""

    return (
        WATER_DENSITY
        * fluid_velocity
        * hydraulic_diameter
        / WATER_DYNAMIC_VISCOSITY)


def pressure_loss_from_pipe_reduction(
        larger_diameter, fluid_velocity,
        reynolds_number, smaller_diameter):
    """Calculate pressure loss from a pipe diameter reduction."""

    k = (
        0.1 + 50 / reynolds_number) * (
        (larger_diameter / smaller_diameter) ** 4 - 1 )

    return (
        -k
        * WATER_DENSITY
        * fluid_velocity ** 2
        / 2000)


def kpa_to_psi(pressure):
    """Convert kilopascals to pounds per square inch."""
    return pressure * 0.1450377


if __name__ == "__main__":
    main()
