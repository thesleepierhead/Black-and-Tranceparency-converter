# Black and Transparency converter 
<br/>
This is a program meant to convert color or grayscale images into ones only made of black pixels of varying transparency. 
<br/><br/>

## What does that mean?

<br/>
Suppose I want to change the background in this scanned drawing I made (or color it in using a layer underneath, could be anything)<br/>
<img src ="examplepictures/original.png" width=300 height=300><br/><br/>

Here's the different options for how I could do that in most raster editing software:
<br/>
|Using the blending options in Photoshop with a low threshold| Using the blending options in Photoshop with a high threshold| Using the magic wand to select the background<br/>|
|----|----|----|
|<img src="examplepictures/blendopt2.png" width=300 height=300>| <img src="examplepictures/blendopt1.png" width=300 height=300>|<img src="examplepictures/magic-wand.png" width=300 height=300>|

<br/>

If you use this program though, you keep all the detail while still avoiding the gray pixel artefacts: 
<br/>
|Grayscale as seen by the human eye| Grayscale without correcting for the eye|
|---|---|
|<img src="examplepictures/grayscale-withbackground.png" width=300 height=300>|<img src="examplepictures/nohue-withbackground.png" width=300 height=300>|

<br/>

What's the difference between "Greyscale as seen by the human eye" and " Greyscale without correcting for the eye"? <br/>
Well, it's more clear if you look at these pictures:
|Grayscale as seen by the human eye|Original| Grayscale without correcting for the eye|
|:---:|:---:|:---:|
|<img src="examplepictures/color-bars1.png" width=100 height=300 >|<img src="examplepictures/color-bars.png" width=100 height=300>|<img src="examplepictures/color-bars2.png" width=100 height=300>|
|This version renders how pure blue looks darker than pure yellow, it's a more intuitive way to converting to greyscale|The original contains two rows, one with pure hues, and another of darker colors|This version renders pure colors as white, which makes it more helpful if you're trying to recolor something|
