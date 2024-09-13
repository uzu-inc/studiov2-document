# General: Setting Conditions

On almost every editing screen, you will encounter the "Setting Conditions" feature, which applies to characters' missions, phases, text, clues, rooms, and game flow. Familiarize yourself with the types and meanings of these conditions to set them appropriately.

## Types and Meanings of Conditions

### New Design

<table><thead><tr><th width="166">Major Category</th><th width="271">Suffix</th><th>Meaning</th></tr></thead><tbody><tr><td>Phase Progress</td><td>During ~</td><td>Texts and BGM are displayed or played only during the relevant phase<br>Clues are distributed during the relevant phase and remain unless collected</td></tr><tr><td></td><td>Not during ~</td><td>Texts and BGM are displayed or played only when the relevant phase is not in progress<br>Clues are distributed when the phase is not in progress and remain unless collected</td></tr><tr><td></td><td>~ has started</td><td>Texts, clues, and BGM are displayed or played from the start of the phase until they are stopped</td></tr><tr><td></td><td>~ has ended</td><td>Texts, clues, and BGM are displayed or played immediately after the phase ends until they are stopped</td></tr><tr><td></td><td>~ was not stepped on</td><td>Indicates that a certain phase has not yet been reached or a certain route among multiple routes has not been taken</td></tr><tr><td>Voting Results</td><td>~ got the most votes in ○</td><td>Literally as stated</td></tr><tr><td></td><td>~ got the most votes alone in ○</td><td>Literally as stated</td></tr><tr><td>Voting Action</td><td>□ voted for ~ in ○</td><td>Focuses not on vote tallying but on specifying individual voting targets, differing from the above two</td></tr><tr><td>Clues</td><td>□ revealed △</td><td>The clue is publicly revealed</td></tr><tr><td></td><td>□ possesses △</td><td>The clue is possessed (not just viewable)</td></tr><tr><td></td><td>□ viewed △</td><td>Among clues that are neither publicly revealed nor possessed, those that have been viewed (shown by someone or originally possessed and then transferred)</td></tr><tr><td>Call Room</td><td>Only while □ is in ◇</td><td>Texts and BGM are displayed or played only while in the specific room<br>Clues are distributed while in the room and remain unless collected</td></tr><tr><td>Cue</td><td>~ has started</td><td>At any point after the start of the reading</td></tr><tr><td>Action Action</td><td>□ executed ▽</td><td>Whether the action execution button has been pressed or not</td></tr></tbody></table>

Furthermore, the new design includes numerical comparison conditions as follows.

<table><thead><tr><th width="201">Type</th><th>Item to Compare</th><th>Comparison Target</th></tr></thead><tbody><tr><td>Votes Count</td><td>Number of votes for any option in any voting phase</td><td>Any number</td></tr><tr><td></td><td></td><td>Number of votes for any other option in the same voting phase</td></tr><tr><td>Action Execution Count</td><td>How many times any character has executed any action</td><td>Any number</td></tr><tr><td>Token Possession Count</td><td>Number of tokens a particular character possesses</td><td>Any number</td></tr><tr><td></td><td></td><td>Number of tokens a specific character possesses</td></tr><tr><td>Phase Loop Count</td><td>How many times a particular phase has been passed</td><td>Any number</td></tr></tbody></table>

#### Condition Groups

In some settings, you can also use condition groups. With condition groups, you can set **complex conditions using 'and' and 'or'**.

To change to a condition group, add the condition as usual and then click the '...' that appears in the top right corner of the condition. If clicking '...' does not suggest changes, condition groups are not available.

Currently, condition groups can be set up to three levels.

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

### Old Design

Note that the contents are generally the same, but old and new designs coexist.

Here are the 8 types of conditions that can be set. For every 'during ~', a 'not during ~' condition can also be used, and similarly for 'when ~' and 'when not ~'.

| Item                                               | Basic Content                                                                             | Other                                                                          |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Only during a specific phase                       | Texts and rooms are displayed only during that phase and disappear once the phase ends.   | Clues can only be obtained during that phase and once obtained remain in hand. |
| Has reached a specific phase                       | Distribution and display apply from the moment that phase begins.                         | Distribution and display continue even after the phase.                        |
| A specific phase has ended                         | Distribution and display start after the phase ends.                                      | Suitable for read-through distribution.                                        |
| A certain option has the most votes                | Both sole majority and tie majority can be selected, mainly used for branching processes. | Tie majority means 'considered the most even in a tie'.                        |
| A certain character has voted for a certain option | Literally as stated. Used for branching processes and distribution of information.        | Also plays a role in achieving detective missions.                             |
| A certain character possesses a certain clue       | Literally as stated. Used for determining additional information distribution.            | Also plays a role in achieving collection missions.                            |
| A certain character is in a certain room           | Conditions can be based on whether a character is in a specific call room.                | -                                                                              |
| Character conditions                               | You can select the characters to apply conditions to using checkboxes.                    | -                                                                              |

**and (and)**\
Please understand it in a mathematical sense of 'happening simultaneously' or 'both being fulfilled'. It's not just a simple 'and' like A&B.

**or (or)**\
Refers to 'if either occurs'.
