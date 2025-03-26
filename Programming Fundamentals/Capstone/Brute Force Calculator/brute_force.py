import sys

# Constants
SECONDS_IN_A_YEAR = 31536000 # Seconds in a year
FLOPS_PER_CHECK = 1000 # Amount per single key check

# Function to calculate time to brute force
def GetBruteForce(key_size, giga_flops):
    # Calculate the number of possible keys
    num_keys = 2 ** key_size

    # Calculate the time required for a single key attempt
    time_per_attempt = FLOPS_PER_CHECK / (giga_flops * (10**9))

    # Calculate the total time required for a brute force attack
    total_time = (num_keys * time_per_attempt) / SECONDS_IN_A_YEAR

    # Time returned (in years)
    return total_time

def main():
    # Validate Input
    if len(sys.argv) != 3: # Only script name and 2 arguments
        print('Usage: brute_force.py <key size> <giga flops>')
        sys.exit(1)

    # Assign input variables
    try:
        program_name = sys.argv[0]
        key_size = int(sys.argv[1])
        giga_flops = int(sys.argv[2])
    except ValueError:
        print('Error: Key size and giga flops must be integers.')
    
    # Calculate Best/Avg/Worst Case (in years)
    best_case = GetBruteForce(0, giga_flops) # A single check is best case
    average_case = GetBruteForce(key_size, giga_flops) * 0.5 # Avg is about half
    worst_case = GetBruteForce(key_size, giga_flops) # Most time

    # Print formatted results
    print('Running', program_name, 'for a', key_size, 'byte key @', giga_flops,"gigaflops.")
    print(f"Best Case Years to Crack: {best_case:.16} years")
    print(f"Average Case Years to Crack: {average_case:.16} years")
    print(f"Worst Case Years to Crack: {worst_case:.16} years")

main()