import os
import pandas as pd

directory = os.path.dirname(__file__)
path = os.path.join(directory, 'election_data.csv')

data_df = pd.read_csv(path)
print(data_df.head())


total_votes = len(data_df['Voter ID'])
candidates = []
vote_counts = []
percentage = []
winner = []
winning_count = 0

for value in data_df['Candidate']:
    if value not in candidates:
        candidates.append(value)

for name in candidates:
    candidate_df = data_df.loc[data_df['Candidate'] == name]
    vote_count = len(candidate_df['Voter ID'])
    vote_counts.append(vote_count)

for value in vote_counts:
    share = value/total_votes*100
    percentage.append(share)

final_df = {'Candidate': candidates,
            'Vote count': vote_counts,
            'Percentage': percentage}

final_df = pd.DataFrame(final_df)

with open(directory + '/results.txt', 'w') as file:
    results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
        f"")
    file.write(results)
    print(results)

    for i in range(0, len(final_df['Candidate'])):
        name = final_df['Candidate'][i]
        vote_percentage = final_df['Percentage'][i]
        votes = final_df['Vote count'][i]
        output = f"{name}: {vote_percentage:.3f}% ({votes})\n"
        file.write(output)
        print(output)

        if votes > winning_count:
            winning_count = votes
            winner = name
            winner_output = (
                f"-------------------------\n"
                f"Winner: {winner}\n"
                f"-------------------------\n")

    file.write(winner_output)
    print(winner_output)

