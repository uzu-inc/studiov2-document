# Background Image

You can set the background image for the play screen.

### Default Background

<figure><img src="../.gitbook/assets/screenshot 2024-01-31 14.53.39.png" alt=""><figcaption></figcaption></figure>

The default background is an image that continues to be displayed when no conditional background is set or the conditions for the conditional background are not met.

Images can be set by dropping or clicking.

If no default background is set in the work, a plain background matching the color theme is automatically applied.

Once the image is set, it will look like the following, and you can verify that the background image has been set by performing an operational check.

A color blur that matches the color theme (white in light mode, black in dark mode, etc.) is automatically applied to the background image. The blur is set to a density that ensures text readability regardless of the background image uploaded. Since text readability is a prerequisite for the Madamis app, you cannot turn off the blur.

<figure><img src="../.gitbook/assets/screenshot 2024-01-31 15.04.30.png" alt=""><figcaption></figcaption></figure>

<div align="left">

<figure><img src="../.gitbook/assets/screenshot 2024-01-31 15.05.58.png" alt="" width="179"><figcaption></figcaption></figure>

</div>

### Conditional Background

The conditional background is a background that is displayed when certain conditions are met.

Setting an image in "Conditional Background" allows you to set conditions.

<figure><img src="../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

Be careful because if the conditions are met, that image will always be displayed. For example, if the condition is "When phase XX starts," the conditional image will continue to be displayed even after that phase ends. If you want to set a background image for only a specific phase, it would be better to set it as "While phase XX is in progress."

This time, I have set it to display the conditional image only during the opening.

<figure><img src="../.gitbook/assets/screenshot 2024-01-31 15.17.19.png" alt=""><figcaption></figcaption></figure>

When performing an operational check, you can see that the image changes only during the opening phase.

<div>

<figure><img src="../.gitbook/assets/screenshot 2024-01-31 15.18.44.png" alt="" width="182"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/screenshot 2024-01-31 15.18.51.png" alt="" width="176"><figcaption></figcaption></figure>

</div>

Multiple conditional backgrounds can be set, but priority is given from left to right.
