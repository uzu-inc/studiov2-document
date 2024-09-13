# Incorporating an Investigation Phase

By combining a voting phase with clue distribution, you can create an investigation phase.

For investigations using decks, please refer to [this page](../basic-features/decks.md).

<figure><img src="../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

\

## ① Creating the Phase

From the phase list, click "Add Phase" and select the "Voting" phase.

Within the voting phase you created, set the options for investigation locations.

Since multiple players investigating the same location reduces the number of clues they can gather, it’s advisable to allow players to view which locations others have voted for.

\

Additionally, by clicking "Prohibit duplicate votes for this option" under "Selection Conditions," you can prevent more than one player from voting for the same option. This is effective when you want each player to investigate different locations without overlap.

During gameplay, the options chosen by others will appear dimmed on the screens of the remaining players.

_Note: Currently, "Prohibit duplicate votes for this option" cannot be combined with other conditions using "and" or "or."_

<figure><img src="../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

\

## ② Creating Clues

From the clue list, click "Add New" and create clues corresponding to the investigation locations set in step ①.

Set up the clue distribution for each player as follows:

| Item                    | Content                                                 | Details                                                                                                                                   |
| ----------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Condition 1 (if needed) | Phase Progress・When ○○ starts                          | This is the phase where clues will be distributed. It’s best to use the last of the consecutive voting phases or the discussion phase.    |
| Condition 2             | Voting Action・When ○○ voted for △△ in the voting phase | Set the condition that a specific character has voted for the corresponding investigation location in the voting phase created in step ①. |
| Distribution Method     | Transfer ownership in an unpublished state              | －                                                                                                                                        |
| Distribution Target     | Select a character                                      | Match this to the character from Condition 2.                                                                                             |

\

For conditions like public display, sharing, or transfer, it’s a good idea to set the discussion phase under "Phase Progress・When ○○ starts."
