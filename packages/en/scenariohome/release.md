# Release Management

The "Release Management" screen in Uzu Studio allows you to **check versions**, **submit for review**, and **copy IDs needed for test play**.

## Version Checking

For scenarios that have passed the review and been published in the app, there are two versions: "Published in the App" and "Test Play." (For unpublished scenarios, the labels may differ slightly, but the concept is the same.)

If you make any content corrections (such as typos) in Uzu Studio after submitting for review, be sure to **create the latest version and click "Update Published (Planned) Version"** to apply the changes.

If you make major changes to the phases or actions (not just minor text corrections), always run a function test before clicking the update button.

<table>
<thead>
<tr><th width="180.33333333333331">Version</th><th>Details</th></tr>
</thead>
<tbody>
<tr><td>Published in the App</td><td>The version that anyone can play by clicking "Play this scenario" in the app.<br>Updates will be reflected when the update button is clicked.</td></tr>
<tr><td>Test Play</td><td>A version that can only be used to create events by Uzu accounts linked to the author's Uzu Studio account.<br>When this version is active, the author will see two event creation buttons on the scenario details screen in the Uzu app.</td></tr>
</tbody>
</table>

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

### Reflecting Version Updates

- **Events created after clicking the update button**: The latest version with corrections will be played.
- **Events created before clicking the update button but starting 6 hours after the update**: The latest version with corrections will be played.
- **Events created before clicking the update button and starting within 6 hours of the update**: The old version without corrections will be played.

### More on the Test Play Version

This version is exclusively for test play, allowing only the author to create events. General users cannot play this version.

In v2, there is more freedom compared to v1, resulting in more settings to manage and potential for mistakes. Therefore, before releasing the public version, a test play version is created to ensure no major issues remain.

After reviewing and verifying the content, click the update button in the version management screen to publish the scenario in the app for general users. For works transitioning from v1 to v2, **the update button cannot be clicked until the migration request is approved**.

## Limited Link Access

Limited Link Access allows a scenario that is not publicly listed in Uzu (i.e., not visible in the scenario list or searchable) to be playable by anyone who knows the URL.

Keep in mind that if this feature is turned on, anyone with the URL can play the scenario, even during testing or while the scenario is under development. It is generally recommended to keep this feature off unless you have a specific reason for enabling it.

Use cases for Limited Link Access include having others test play the scenario without the author's observation or sharing a private scenario with a small group of acquaintances.

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Review Submission

You can submit your work for review by clicking the **"Submit for App Listing"** button.

There are two types of reviews: **Basic Review** for scenarios that will be free, and **Detailed Review** for scenarios that will be paid. After clicking the submission button, select the appropriate review type in the following **form** and fill out the required information.

_Note: You can continue to edit your scenario after submitting for review, but the review will be conducted based on the content available in Uzu Studio at the time the reviewer checks the scenario._

## Copying Scenario ID

To view a scenario that is still in the test play phase and not yet publicly listed in Uzu, you'll need the scenario's ID (an alphanumeric string). Copy this ID from the screen shown below.

For more information on test plays, please refer to [this page](../overview/makingflow/testplay.md).

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>
