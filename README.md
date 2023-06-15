# ChromeFlagEmojis

Chrome Extension that replaces Unicode Regional Indicators with images of actual flags. (Note: Which Flags are included has nothing to do with any personal political opinions and is defined only by what the Unicode consortium recommends for [General Interchange](https://unicode.org/emoji/charts/emoji-zwj-sequences.html))

## Overview

Makes flags in text look like this:

![image](https://github.com/Brxnni/ChromeFlagEmojis/assets/72916383/5faa91de-edc3-4a45-a6dd-a0cb45376f24)

Instead of this:

![image](https://github.com/Brxnni/ChromeFlagEmojis/assets/72916383/750ec6fa-377c-4922-b38a-ca71ee6a7b28)

Style Size and Position of Flags can be changed.

Styles available: Apple/Google/Samsung/WhatsApp/Twitter/Facebook/OpenMoji
![image](https://github.com/Brxnni/ChromeFlagEmojis/assets/72916383/99a8e122-1cc2-41ce-a749-3a3c45fb5e6b)

## TODO

* Fix bug where sometimes a comment that has flags from the previous page you were on is mixed with the first comment on the current video (????)
* Deactivate the conversion in textfields (extension currently breaks the github code editor for example)
  * Could be detected by listeningn events and seeing if target is TEXTAREA or something like that -> Put it on the list of elements to ignore
* Add On/Off button
* Add offline option
* Reload images when the first load fails
* Add other subdivions? There are a couple that only OpenMoji supports (California, Texas, Bretagne, Catalonia, Basque Country, Quebec, Berlin, Asturias)
