import os
import csv

# File path
poll_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')
output_file = os.path.join('PyPoll', 'analysis', 'election_results.txt')

# Initialize variables
total_votes = 0
candidates = []
votes_per_candidate = {}

# Open the CSV file
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    next(csvreader)

    # Iterate over each row in the CSV
    for row in csvreader:
        # Increment total votes
        total_votes = total_votes + 1

        # Extract candidate name
        candidate = row[2]

        # Add candidate to the list if not already present
        if candidate not in candidates:
            candidates.append(candidate)
            votes_per_candidate[candidate] = 0

        # Increment vote count for the candidate
        votes_per_candidate[candidate] += 1

# Calculate percentage of votes for each candidate
percentage_per_candidate = {candidate: (votes / total_votes) * 100 for candidate, votes in votes_per_candidate.items()}

# Find the winner
winner = max(votes_per_candidate, key=votes_per_candidate.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentage_per_candidate[candidate]:.3f}% ({votes_per_candidate[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write results to a file
with open(output_file, "w", newline='') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidates:
         txtfile.write(f"{candidate}: {percentage_per_candidate[candidate]:.3f}% ({votes_per_candidate[candidate]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
