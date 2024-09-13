---
description: You can set various actions beyond simple clue acquisition and deck investigation.
---

# Actions

## Creating New Actions & Types

Navigate to "Actions" from the left menu.

Click "Add Action" to choose the type of action, and you can create a new one.

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

There are currently two types of actions available (as of 2023.12.7).

<table><thead><tr><th width="141">Name</th><th>Description</th></tr></thead><tbody><tr><td><a href="action.md#shinpuruakushonno">Simple</a></td><td>Triggered by simply pressing "Execute"</td></tr><tr><td><a href="action.md#pasuwdoakushonno">Password</a></td><td>Pressing "Execute" prompts for a password input, and the action is activated if the correct password is entered</td></tr></tbody></table>

<figure><img src="../.gitbook/assets/image (54).png" alt="" width="563"><figcaption></figcaption></figure>

## List of Configurable Actions

As of 2023.12.7, the following actions can be set:

<table><thead><tr><th width="226">Item</th><th>Description</th></tr></thead><tbody><tr><td>Send Notification</td><td>Sends a text notification at the top of the screen when the action is executed.</td></tr><tr><td>Play Sound Effect</td><td>Plays a sound effect when the action is executed.</td></tr><tr><td>Reveal Clue</td><td>Reveals a specific clue to everyone. Ownership is not transferred.</td></tr><tr><td>Phase Transition</td><td>Forcibly transitions to a specific phase.<br>For example, it's recommended to use this in scenarios like the reasoning announcement phase where it's acceptable for one player to decide to move to the next phase.</td></tr><tr><td>Clue Ownership</td><td>Distributes a specific clue to a character.</td></tr><tr><td>Clue Viewing Rights</td><td>Grants viewing rights for a specific clue to a character.</td></tr><tr><td>Move to Chat Room</td><td>Forcibly moves to a specific chat room.</td></tr></tbody></table>

## Setting Simple Actions

### In the Action Editing Screen

- **Title**: The title of the action. Check how it will be displayed in the preview on the right side.
- **Description**: Since the action button is fixed to "**Execute**," write a description that fits this wording.
- **Action Execution Conditions**: If it's just restricting to characters, it can be easily done with checkboxes. For more detailed settings, use "[**Advanced Settings**](action.md#na)."
- **Result Action**: Sets what happens when "Execute" is pressed. For instance, in the image example, it's set to distribute a specific clue when executed.

<figure><img src="../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

#### Setting Multiple Result Actions

As shown in the following image, multiple result actions can be set.

These will be executed all at once as a series of actions when the player presses the "Execute" button once. They are processed in order from top to bottom, so if you want to process them in the order of "distribute clue → send notification," set them up that way in this screen.

<figure><img src="../.gitbook/assets/image (59).png" alt="" width="515"><figcaption></figcaption></figure>

### Placement of Actions (In Clues/Phases)

Actions don't appear during the game just by being set in the action editing screen. You need to configure where the created actions will be placed.

They can be placed in two locations: "within a clue" and "within a basic phase." Here, we'll discuss placing them "within a clue." For placing them "within a basic phase," please refer to [here](action.md#akushonnofzugakarideno-1).

For instance, you want to place an action called "View Contents (add distribution of the first page's content)" within a clue called "Diary."

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

1. Navigate to "Clues" from the left menu.
2. Move to the editing screen of the clue where you want to place the action.
3. Click "Add" in the action section.
4. Select the desired action and click "Decide."

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure>

If it appears as shown below, it's successful.

<figure><img src="../.gitbook/assets/image (58).png" alt="" width="563"><figcaption></figcaption></figure>

## Setting Password Actions

### In the Action Editing Screen

- **Title**: The title of the action. Check how it will be displayed in the preview on the right side.
- **Description**: Since the action button is fixed to "**Execute**," write a description that fits this wording.
- **Answer**: Enter the correct password. You can set multiple entries separated by commas. White spaces are ignored.
  - Adding an Answer Tab allows you to set reactions for each input, such as returning "Good morning" when "Good morning" is entered, and "Hello" when "Hello" is entered.
- **Action Execution Conditions**: If it's just restricting to characters, it can be easily done with checkboxes. For more detailed settings, use "[**Advanced Settings**](action.md#na)."
- **Result Action**: Sets what happens when "Execute" is pressed. It's divided into scenarios where the password is entered correctly and where it's not.
  - **Common Tab**: If there are multiple correct answer tabs set, and they share common result actions, set them in the common tab. For example, if entering a correct answer first triggers a sound effect, then depending on the input, the actions are divided, set "Sound Effect" in the common tab, and set each result action for Answer 1 onwards.

<figure><img src="../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

In the image example, the contents of the result actions are as follows.

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

### Placement of Actions (In Clues/Phases)

Actions don't appear during the game just by being set in the action editing screen. You need to configure where the created actions will be placed.

They can be placed in two locations: "within a clue" and "within a basic phase." Here, we'll discuss placing them "within a basic phase." For placing them "within a clue," please refer to [here](action.md#akushonnogakarifzudeno).

For instance, you want to place an action that allows opening a safe with a password during the "Discussion Phase."

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="563"><figcaption></figcaption></figure>

1. Navigate to "Phases" from the left menu.
2. Move to the basic phase (like the Discussion Phase) where you want to place the action.
3. Click the "Add" button at the bottom of the phase content.
4. Select "Action."
5. Check the corresponding action and click "Decide."

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

If it is added properly as shown below, it's successful.

<figure><img src="../.gitbook/assets/image (66).png" alt="" width="563"><figcaption></figcaption></figure>

## Advanced Edition: Setting Advanced Execution Conditions

We will explain advanced condition settings that can be used for both simple and password actions.

### Limiting Action Execution to Once

If no conditions are set, anyone can execute the action any number of times after a successful execution.

For example, if you set an action to distribute a specific clue to the executor when "Execute" is pressed, after Mr. A executes it, if Mr. B executes it, the clue will move from Mr. A's possession to Mr. B's (because the action overwrites the previous execution).

To avoid such situations, you need to set conditions that prevent the action from being executed again after a successful execution. Here's an example of how to set this up.

**For a Simple Action**

<figure><img src="../.gitbook/assets/image (67).png" alt="" width="563"><figcaption></figcaption></figure>

**For a Password Action**

If you set it up the same way as the simple action, even an incorrect password input would count as "executed," and afterwards, no one else would be able to attempt to input the password, so a bit of customization is necessary in the settings.

<figure><img src="../.gitbook/assets/image (68).png" alt="" width="563"><figcaption></figcaption></figure>

### Other Limitations

You can also set conditions such as "only during a certain phase," "only when in a certain chat room," "only if the person has a certain clue," etc.

Utilize these settings according to the content of your scenario.
