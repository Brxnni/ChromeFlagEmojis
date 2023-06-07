# ChromeFlagEmojis

Chrome Extension that replaces Unicode Regional Indicators with images of actual flags.

## Preview

Looks like this:

![image](https://github.com/Brxnni/ChromeFlagEmojis/assets/72916383/5faa91de-edc3-4a45-a6dd-a0cb45376f24)

Instead of this:

![image](https://github.com/Brxnni/ChromeFlagEmojis/assets/72916383/750ec6fa-377c-4922-b38a-ca71ee6a7b28)

Looks good with all fonts and font sizes:

![image](https://github.com/Brxnni/ChromeFlagEmojis/assets/72916383/76ab97c4-ff56-4c8c-872b-feff4a1377f7)

Style (Twitter/Apple etc.), Size and Position of Flags can be changed.

Twitter: <img src="https://em-content.zobj.net/thumbs/120/twitter/322/flag-estonia_1f1ea-1f1ea.png" width="24" />

Apple: <img src="https://em-content.zobj.net/thumbs/120/apple/354/flag-estonia_1f1ea-1f1ea.png" width="24" />

Google: <img src="https://em-content.zobj.net/thumbs/120/google/350/flag-estonia_1f1ea-1f1ea.png" width="24" />

OpenMoji: <img src="https://em-content.zobj.net/thumbs/120/openmoji/338/flag-estonia_1f1ea-1f1ea.png" width="24" />

And a couple more.

## TODO

* Fix bug where sometimes a comment that has flags from the previous page you were on is mixed with the first comment on the current video (????)
* Deactivate the conversion in textfields (extension currently breaks the github code editor for example)
  * Could be detected by listening for keydown events and seeing if target is TEXTAREA or something like that -> Put it on the list of elements to ignore
* Add subdivisions? (UK ones are the only ones supported by most vendors)
* Add On/Off button
