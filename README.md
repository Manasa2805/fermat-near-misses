# Opening comment
# Title: Near Misses Finder for Fermat's Last Theorem
# Authors: Your Name, Partner's Name
# Email: your.email@example.com, partner.email@example.com
# Course: Course Number and Section
# Date: Submission Date
# Description: This program finds near misses for Fermat's Last Theorem.

def main():
    n = int(input("Enter n (2 < n < 12): "))
    k = int(input("Enter k (k > 10): "))
    
    smallest_miss = float('inf')
    best_x, best_y, best_z = None, None, None

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            value = x**n + y**n
            z = int(value ** (1/n))  # Find z
            miss_z = abs(value - z**n)
            miss_z1 = abs(value - (z + 1)**n)
            
            # Calculate the smallest miss and relative miss
            if miss_z < miss_z1:
                miss = miss_z
            else:
                miss = miss_z1
            
            relative_miss = miss / value

            if relative_miss < smallest_miss:
                smallest_miss = relative_miss
                best_x, best_y, best_z = x, y, z

            # Print the current results
            print(f"x: {x}, y: {y}, z: {best_z}, Miss: {miss}, Relative Miss: {relative_miss}")

    print(f"Smallest Relative Miss: {smallest_miss} found at x: {best_x}, y: {best_y}, z: {best_z}")

if __name__ == "__main__":
    main()
