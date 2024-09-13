# Implementing a Rescue Phase When Proceeding Before Everyone Has Completed the Investigation

In UZU, where it is not possible to go back to the previous phase, moving forward without completing all clue gathering may result in missing necessary information.

To avoid this, here is how to implement a rescue phase for situations where the investigation was forgotten or incomplete.

## Pattern 1: Always Go Through the Rescue Phase

Difficulty: Low

<figure><img src="../.gitbook/assets/image (78).png" alt="" width="563"><figcaption></figcaption></figure>

① Create an investigation phase with explanations and the deck of clues.

② Copy that investigation phase and make it the rescue phase. It's a good idea to add a message like "If you didn't finish the investigation in the previous phase, please gather the clues here" (you can write it however you like).

③ Simply place and link the original investigation phase and the rescue phase in sequence, as shown in the diagram, to complete the setup.

## Pattern 2: Only Go to the Rescue Phase When the Investigation is Incomplete

Difficulty: Medium to High

<figure><img src="../.gitbook/assets/image (79).png" alt="" width="563"><figcaption></figcaption></figure>

① Create an investigation phase with explanations and the deck of clues.

② Copy that investigation phase and make it the rescue phase. It's a good idea to add a message like "It seems someone hasn't finished the investigation. Please gather the clues here" (you can write it however you like).

③ Link the investigation phase and the next phase (in the diagram, "Discussion 1") as normal.

④ Set it up so that if certain conditions are met, players will detour to the rescue phase before moving to the next phase (in the diagram, "Discussion 1").

⑤ As the condition for going to the rescue phase, set it to "When the investigation is incomplete (e.g., clues not collected)." This completes the setup.

<figure><img src="../.gitbook/assets/image (80).png" alt="" width="563"><figcaption></figcaption></figure>
