import os
import requests

path = os.path.dirname(os.path.abspath(__file__))
flag_path = os.path.join(path, "src", "flags")

url = "https://em-content.zobj.net/thumbs/120/%s/%s/flag-%s_%s.png"
flagNames = {
	"1f1e6-1f1e8": { "fullName": "Ascension Island", "shortName": "ascension-island" },
	"1f1e6-1f1e9": { "fullName": "Andorra", "shortName": "andorra" },
	"1f1e6-1f1ea": { "fullName": "United Arab Emirates", "shortName": "united-arab-emirates" },
	"1f1e6-1f1eb": { "fullName": "Afghanistan", "shortName": "afghanistan" },
	"1f1e6-1f1ec": { "fullName": "Antigua & Barbuda", "shortName": "antigua-barbuda" },
	"1f1e6-1f1ee": { "fullName": "Anguilla", "shortName": "anguilla" },
	"1f1e6-1f1f1": { "fullName": "Albania", "shortName": "albania" },
	"1f1e6-1f1f2": { "fullName": "Armenia", "shortName": "armenia" },
	"1f1e6-1f1f4": { "fullName": "Angola", "shortName": "angola" },
	"1f1e6-1f1f6": { "fullName": "Antarctica", "shortName": "antarctica" },
	"1f1e6-1f1f7": { "fullName": "Argentina", "shortName": "argentina" },
	"1f1e6-1f1f8": { "fullName": "American Samoa", "shortName": "american-samoa" },
	"1f1e6-1f1f9": { "fullName": "Austria", "shortName": "austria" },
	"1f1e6-1f1fa": { "fullName": "Australia", "shortName": "australia" },
	"1f1e6-1f1fc": { "fullName": "Aruba", "shortName": "aruba" },
	"1f1e6-1f1fd": { "fullName": "Åland Islands", "shortName": "aland-islands" },
	"1f1e6-1f1ff": { "fullName": "Azerbaijan", "shortName": "azerbaijan" },
	"1f1e7-1f1e6": { "fullName": "Bosnia & Herzegovina", "shortName": "bosnia-herzegovina" },
	"1f1e7-1f1e7": { "fullName": "Barbados", "shortName": "barbados" },
	"1f1e7-1f1e9": { "fullName": "Bangladesh", "shortName": "bangladesh" },
	"1f1e7-1f1ea": { "fullName": "Belgium", "shortName": "belgium" },
	"1f1e7-1f1eb": { "fullName": "Burkina Faso", "shortName": "burkina-faso" },
	"1f1e7-1f1ec": { "fullName": "Bulgaria", "shortName": "bulgaria" },
	"1f1e7-1f1ed": { "fullName": "Bahrain", "shortName": "bahrain" },
	"1f1e7-1f1ee": { "fullName": "Burundi", "shortName": "burundi" },
	"1f1e7-1f1ef": { "fullName": "Benin", "shortName": "benin" },
	"1f1e7-1f1f1": { "fullName": "St. Barthélemy", "shortName": "st-barthelemy" },
	"1f1e7-1f1f2": { "fullName": "Bermuda", "shortName": "bermuda" },
	"1f1e7-1f1f3": { "fullName": "Brunei", "shortName": "brunei" },
	"1f1e7-1f1f4": { "fullName": "Bolivia", "shortName": "bolivia" },
	"1f1e7-1f1f6": { "fullName": "Caribbean Netherlands", "shortName": "caribbean-netherlands" },
	"1f1e7-1f1f7": { "fullName": "Brazil", "shortName": "brazil" },
	"1f1e7-1f1f8": { "fullName": "Bahamas", "shortName": "bahamas" },
	"1f1e7-1f1f9": { "fullName": "Bhutan", "shortName": "bhutan" },
	"1f1e7-1f1fb": { "fullName": "Bouvet Island", "shortName": "bouvet-island" },
	"1f1e7-1f1fc": { "fullName": "Botswana", "shortName": "botswana" },
	"1f1e7-1f1fe": { "fullName": "Belarus", "shortName": "belarus" },
	"1f1e7-1f1ff": { "fullName": "Belize", "shortName": "belize" },
	"1f1e8-1f1e6": { "fullName": "Canada", "shortName": "canada" },
	"1f1e8-1f1e8": { "fullName": "Cocos (Keeling) Islands", "shortName": "cocos-keeling-islands" },
	"1f1e8-1f1e9": { "fullName": "Congo - Kinshasa", "shortName": "congo-kinshasa" },
	"1f1e8-1f1eb": { "fullName": "Central African Republic", "shortName": "central-african-republic" },
	"1f1e8-1f1ec": { "fullName": "Congo - Brazzaville", "shortName": "congo-brazzaville" },
	"1f1e8-1f1ed": { "fullName": "Switzerland", "shortName": "switzerland" },
	"1f1e8-1f1ee": { "fullName": "Côte d’Ivoire", "shortName": "cote-divoire" },
	"1f1e8-1f1f0": { "fullName": "Cook Islands", "shortName": "cook-islands" },
	"1f1e8-1f1f1": { "fullName": "Chile", "shortName": "chile" },
	"1f1e8-1f1f2": { "fullName": "Cameroon", "shortName": "cameroon" },
	"1f1e8-1f1f3": { "fullName": "China", "shortName": "china" },
	"1f1e8-1f1f4": { "fullName": "Colombia", "shortName": "colombia" },
	"1f1e8-1f1f5": { "fullName": "Clipperton Island", "shortName": "clipperton-island" },
	"1f1e8-1f1f7": { "fullName": "Costa Rica", "shortName": "costa-rica" },
	"1f1e8-1f1fa": { "fullName": "Cuba", "shortName": "cuba" },
	"1f1e8-1f1fb": { "fullName": "Cape Verde", "shortName": "cape-verde" },
	"1f1e8-1f1fc": { "fullName": "Curaçao", "shortName": "curacao" },
	"1f1e8-1f1fd": { "fullName": "Christmas Island", "shortName": "christmas-island" },
	"1f1e8-1f1fe": { "fullName": "Cyprus", "shortName": "cyprus" },
	"1f1e8-1f1ff": { "fullName": "Czechia", "shortName": "czechia" },
	"1f1e9-1f1ea": { "fullName": "Germany", "shortName": "germany" },
	"1f1e9-1f1ec": { "fullName": "Diego Garcia", "shortName": "diego-garcia" },
	"1f1e9-1f1ef": { "fullName": "Djibouti", "shortName": "djibouti" },
	"1f1e9-1f1f0": { "fullName": "Denmark", "shortName": "denmark" },
	"1f1e9-1f1f2": { "fullName": "Dominica", "shortName": "dominica" },
	"1f1e9-1f1f4": { "fullName": "Dominican Republic", "shortName": "dominican-republic" },
	"1f1e9-1f1ff": { "fullName": "Algeria", "shortName": "algeria" },
	"1f1ea-1f1e6": { "fullName": "Ceuta & Melilla", "shortName": "ceuta-melilla" },
	"1f1ea-1f1e8": { "fullName": "Ecuador", "shortName": "ecuador" },
	"1f1ea-1f1ea": { "fullName": "Estonia", "shortName": "estonia" },
	"1f1ea-1f1ec": { "fullName": "Egypt", "shortName": "egypt" },
	"1f1ea-1f1ed": { "fullName": "Western Sahara", "shortName": "western-sahara" },
	"1f1ea-1f1f7": { "fullName": "Eritrea", "shortName": "eritrea" },
	"1f1ea-1f1f8": { "fullName": "Spain", "shortName": "spain" },
	"1f1ea-1f1f9": { "fullName": "Ethiopia", "shortName": "ethiopia" },
	"1f1ea-1f1fa": { "fullName": "European Union", "shortName": "european-union" },
	"1f1eb-1f1ee": { "fullName": "Finland", "shortName": "finland" },
	"1f1eb-1f1ef": { "fullName": "Fiji", "shortName": "fiji" },
	"1f1eb-1f1f0": { "fullName": "Falkland Islands", "shortName": "falkland-islands" },
	"1f1eb-1f1f2": { "fullName": "Micronesia", "shortName": "micronesia" },
	"1f1eb-1f1f4": { "fullName": "Faroe Islands", "shortName": "faroe-islands" },
	"1f1eb-1f1f7": { "fullName": "France", "shortName": "france" },
	"1f1ec-1f1e6": { "fullName": "Gabon", "shortName": "gabon" },
	"1f1ec-1f1e7": { "fullName": "United Kingdom", "shortName": "united-kingdom" },
	"1f1ec-1f1e9": { "fullName": "Grenada", "shortName": "grenada" },
	"1f1ec-1f1ea": { "fullName": "Georgia", "shortName": "georgia" },
	"1f1ec-1f1eb": { "fullName": "French Guiana", "shortName": "french-guiana" },
	"1f1ec-1f1ec": { "fullName": "Guernsey", "shortName": "guernsey" },
	"1f1ec-1f1ed": { "fullName": "Ghana", "shortName": "ghana" },
	"1f1ec-1f1ee": { "fullName": "Gibraltar", "shortName": "gibraltar" },
	"1f1ec-1f1f1": { "fullName": "Greenland", "shortName": "greenland" },
	"1f1ec-1f1f2": { "fullName": "Gambia", "shortName": "gambia" },
	"1f1ec-1f1f3": { "fullName": "Guinea", "shortName": "guinea" },
	"1f1ec-1f1f5": { "fullName": "Guadeloupe", "shortName": "guadeloupe" },
	"1f1ec-1f1f6": { "fullName": "Equatorial Guinea", "shortName": "equatorial-guinea" },
	"1f1ec-1f1f7": { "fullName": "Greece", "shortName": "greece" },
	"1f1ec-1f1f8": { "fullName": "South Georgia & South Sandwich Islands", "shortName": "south-georgia-south-sandwich-islands" },
	"1f1ec-1f1f9": { "fullName": "Guatemala", "shortName": "guatemala" },
	"1f1ec-1f1fa": { "fullName": "Guam", "shortName": "guam" },
	"1f1ec-1f1fc": { "fullName": "Guinea-Bissau", "shortName": "guinea-bissau" },
	"1f1ec-1f1fe": { "fullName": "Guyana", "shortName": "guyana" },
	"1f1ed-1f1f0": { "fullName": "Hong Kong SAR China", "shortName": "hong-kong-sar-china" },
	"1f1ed-1f1f2": { "fullName": "Heard & McDonald Islands", "shortName": "heard-mcdonald-islands" },
	"1f1ed-1f1f3": { "fullName": "Honduras", "shortName": "honduras" },
	"1f1ed-1f1f7": { "fullName": "Croatia", "shortName": "croatia" },
	"1f1ed-1f1f9": { "fullName": "Haiti", "shortName": "haiti" },
	"1f1ed-1f1fa": { "fullName": "Hungary", "shortName": "hungary" },
	"1f1ee-1f1e8": { "fullName": "Canary Islands", "shortName": "canary-islands" },
	"1f1ee-1f1e9": { "fullName": "Indonesia", "shortName": "indonesia" },
	"1f1ee-1f1ea": { "fullName": "Ireland", "shortName": "ireland" },
	"1f1ee-1f1f1": { "fullName": "Israel", "shortName": "israel" },
	"1f1ee-1f1f2": { "fullName": "Isle of Man", "shortName": "isle-of-man" },
	"1f1ee-1f1f3": { "fullName": "India", "shortName": "india" },
	"1f1ee-1f1f4": { "fullName": "British Indian Ocean Territory", "shortName": "british-indian-ocean-territory" },
	"1f1ee-1f1f6": { "fullName": "Iraq", "shortName": "iraq" },
	"1f1ee-1f1f7": { "fullName": "Iran", "shortName": "iran" },
	"1f1ee-1f1f8": { "fullName": "Iceland", "shortName": "iceland" },
	"1f1ee-1f1f9": { "fullName": "Italy", "shortName": "italy" },
	"1f1ef-1f1ea": { "fullName": "Jersey", "shortName": "jersey" },
	"1f1ef-1f1f2": { "fullName": "Jamaica", "shortName": "jamaica" },
	"1f1ef-1f1f4": { "fullName": "Jordan", "shortName": "jordan" },
	"1f1ef-1f1f5": { "fullName": "Japan", "shortName": "japan" },
	"1f1f0-1f1ea": { "fullName": "Kenya", "shortName": "kenya" },
	"1f1f0-1f1ec": { "fullName": "Kyrgyzstan", "shortName": "kyrgyzstan" },
	"1f1f0-1f1ed": { "fullName": "Cambodia", "shortName": "cambodia" },
	"1f1f0-1f1ee": { "fullName": "Kiribati", "shortName": "kiribati" },
	"1f1f0-1f1f2": { "fullName": "Comoros", "shortName": "comoros" },
	"1f1f0-1f1f3": { "fullName": "St. Kitts & Nevis", "shortName": "st-kitts-nevis" },
	"1f1f0-1f1f5": { "fullName": "North Korea", "shortName": "north-korea" },
	"1f1f0-1f1f7": { "fullName": "South Korea", "shortName": "south-korea" },
	"1f1f0-1f1fc": { "fullName": "Kuwait", "shortName": "kuwait" },
	"1f1f0-1f1fe": { "fullName": "Cayman Islands", "shortName": "cayman-islands" },
	"1f1f0-1f1ff": { "fullName": "Kazakhstan", "shortName": "kazakhstan" },
	"1f1f1-1f1e6": { "fullName": "Laos", "shortName": "laos" },
	"1f1f1-1f1e7": { "fullName": "Lebanon", "shortName": "lebanon" },
	"1f1f1-1f1e8": { "fullName": "St. Lucia", "shortName": "st-lucia" },
	"1f1f1-1f1ee": { "fullName": "Liechtenstein", "shortName": "liechtenstein" },
	"1f1f1-1f1f0": { "fullName": "Sri Lanka", "shortName": "sri-lanka" },
	"1f1f1-1f1f7": { "fullName": "Liberia", "shortName": "liberia" },
	"1f1f1-1f1f8": { "fullName": "Lesotho", "shortName": "lesotho" },
	"1f1f1-1f1f9": { "fullName": "Lithuania", "shortName": "lithuania" },
	"1f1f1-1f1fa": { "fullName": "Luxembourg", "shortName": "luxembourg" },
	"1f1f1-1f1fb": { "fullName": "Latvia", "shortName": "latvia" },
	"1f1f1-1f1fe": { "fullName": "Libya", "shortName": "libya" },
	"1f1f2-1f1e6": { "fullName": "Morocco", "shortName": "morocco" },
	"1f1f2-1f1e8": { "fullName": "Monaco", "shortName": "monaco" },
	"1f1f2-1f1e9": { "fullName": "Moldova", "shortName": "moldova" },
	"1f1f2-1f1ea": { "fullName": "Montenegro", "shortName": "montenegro" },
	"1f1f2-1f1eb": { "fullName": "St. Martin", "shortName": "st-martin" },
	"1f1f2-1f1ec": { "fullName": "Madagascar", "shortName": "madagascar" },
	"1f1f2-1f1ed": { "fullName": "Marshall Islands", "shortName": "marshall-islands" },
	"1f1f2-1f1f0": { "fullName": "North Macedonia", "shortName": "north-macedonia" },
	"1f1f2-1f1f1": { "fullName": "Mali", "shortName": "mali" },
	"1f1f2-1f1f2": { "fullName": "Myanmar (Burma)", "shortName": "myanmar-burma" },
	"1f1f2-1f1f3": { "fullName": "Mongolia", "shortName": "mongolia" },
	"1f1f2-1f1f4": { "fullName": "Macao Sar China", "shortName": "macao-sar-china" },
	"1f1f2-1f1f5": { "fullName": "Northern Mariana Islands", "shortName": "northern-mariana-islands" },
	"1f1f2-1f1f6": { "fullName": "Martinique", "shortName": "martinique" },
	"1f1f2-1f1f7": { "fullName": "Mauritania", "shortName": "mauritania" },
	"1f1f2-1f1f8": { "fullName": "Montserrat", "shortName": "montserrat" },
	"1f1f2-1f1f9": { "fullName": "Malta", "shortName": "malta" },
	"1f1f2-1f1fa": { "fullName": "Mauritius", "shortName": "mauritius" },
	"1f1f2-1f1fb": { "fullName": "Maldives", "shortName": "maldives" },
	"1f1f2-1f1fc": { "fullName": "Malawi", "shortName": "malawi" },
	"1f1f2-1f1fd": { "fullName": "Mexico", "shortName": "mexico" },
	"1f1f2-1f1fe": { "fullName": "Malaysia", "shortName": "malaysia" },
	"1f1f2-1f1ff": { "fullName": "Mozambique", "shortName": "mozambique" },
	"1f1f3-1f1e6": { "fullName": "Namibia", "shortName": "namibia" },
	"1f1f3-1f1e8": { "fullName": "New Caledonia", "shortName": "new-caledonia" },
	"1f1f3-1f1ea": { "fullName": "Niger", "shortName": "niger" },
	"1f1f3-1f1eb": { "fullName": "Norfolk Island", "shortName": "norfolk-island" },
	"1f1f3-1f1ec": { "fullName": "Nigeria", "shortName": "nigeria" },
	"1f1f3-1f1ee": { "fullName": "Nicaragua", "shortName": "nicaragua" },
	"1f1f3-1f1f1": { "fullName": "Netherlands", "shortName": "netherlands" },
	"1f1f3-1f1f4": { "fullName": "Norway", "shortName": "norway" },
	"1f1f3-1f1f5": { "fullName": "Nepal", "shortName": "nepal" },
	"1f1f3-1f1f7": { "fullName": "Nauru", "shortName": "nauru" },
	"1f1f3-1f1fa": { "fullName": "Niue", "shortName": "niue" },
	"1f1f3-1f1ff": { "fullName": "New Zealand", "shortName": "new-zealand" },
	"1f1f4-1f1f2": { "fullName": "Oman", "shortName": "oman" },
	"1f1f5-1f1e6": { "fullName": "Panama", "shortName": "panama" },
	"1f1f5-1f1ea": { "fullName": "Peru", "shortName": "peru" },
	"1f1f5-1f1eb": { "fullName": "French Polynesia", "shortName": "french-polynesia" },
	"1f1f5-1f1ec": { "fullName": "Papua New Guinea", "shortName": "papua-new-guinea" },
	"1f1f5-1f1ed": { "fullName": "Philippines", "shortName": "philippines" },
	"1f1f5-1f1f0": { "fullName": "Pakistan", "shortName": "pakistan" },
	"1f1f5-1f1f1": { "fullName": "Poland", "shortName": "poland" },
	"1f1f5-1f1f2": { "fullName": "St. Pierre & Miquelon", "shortName": "st-pierre-miquelon" },
	"1f1f5-1f1f3": { "fullName": "Pitcairn Islands", "shortName": "pitcairn-islands" },
	"1f1f5-1f1f7": { "fullName": "Puerto Rico", "shortName": "puerto-rico" },
	"1f1f5-1f1f8": { "fullName": "Palestinian Territories", "shortName": "palestinian-territories" },
	"1f1f5-1f1f9": { "fullName": "Portugal", "shortName": "portugal" },
	"1f1f5-1f1fc": { "fullName": "Palau", "shortName": "palau" },
	"1f1f5-1f1fe": { "fullName": "Paraguay", "shortName": "paraguay" },
	"1f1f6-1f1e6": { "fullName": "Qatar", "shortName": "qatar" },
	"1f1f7-1f1ea": { "fullName": "Réunion", "shortName": "reunion" },
	"1f1f7-1f1f4": { "fullName": "Romania", "shortName": "romania" },
	"1f1f7-1f1f8": { "fullName": "Serbia", "shortName": "serbia" },
	"1f1f7-1f1fa": { "fullName": "Russia", "shortName": "russia" },
	"1f1f7-1f1fc": { "fullName": "Rwanda", "shortName": "rwanda" },
	"1f1f8-1f1e6": { "fullName": "Saudi Arabia", "shortName": "saudi-arabia" },
	"1f1f8-1f1e7": { "fullName": "Solomon Islands", "shortName": "solomon-islands" },
	"1f1f8-1f1e8": { "fullName": "Seychelles", "shortName": "seychelles" },
	"1f1f8-1f1e9": { "fullName": "Sudan", "shortName": "sudan" },
	"1f1f8-1f1ea": { "fullName": "Sweden", "shortName": "sweden" },
	"1f1f8-1f1ec": { "fullName": "Singapore", "shortName": "singapore" },
	"1f1f8-1f1ed": { "fullName": "St. Helena", "shortName": "st-helena" },
	"1f1f8-1f1ee": { "fullName": "Slovenia", "shortName": "slovenia" },
	"1f1f8-1f1ef": { "fullName": "Svalbard & Jan Mayen", "shortName": "svalbard-jan-mayen" },
	"1f1f8-1f1f0": { "fullName": "Slovakia", "shortName": "slovakia" },
	"1f1f8-1f1f1": { "fullName": "Sierra Leone", "shortName": "sierra-leone" },
	"1f1f8-1f1f2": { "fullName": "San Marino", "shortName": "san-marino" },
	"1f1f8-1f1f3": { "fullName": "Senegal", "shortName": "senegal" },
	"1f1f8-1f1f4": { "fullName": "Somalia", "shortName": "somalia" },
	"1f1f8-1f1f7": { "fullName": "Suriname", "shortName": "suriname" },
	"1f1f8-1f1f8": { "fullName": "South Sudan", "shortName": "south-sudan" },
	"1f1f8-1f1f9": { "fullName": "São Tomé & Príncipe", "shortName": "sao-tome-principe" },
	"1f1f8-1f1fb": { "fullName": "El Salvador", "shortName": "el-salvador" },
	"1f1f8-1f1fd": { "fullName": "Sint Maarten", "shortName": "sint-maarten" },
	"1f1f8-1f1fe": { "fullName": "Syria", "shortName": "syria" },
	"1f1f8-1f1ff": { "fullName": "Eswatini", "shortName": "eswatini" },
	"1f1f9-1f1e6": { "fullName": "Tristan Da Cunha", "shortName": "tristan-da-cunha" },
	"1f1f9-1f1e8": { "fullName": "Turks & Caicos Islands", "shortName": "turks-caicos-islands" },
	"1f1f9-1f1e9": { "fullName": "Chad", "shortName": "chad" },
	"1f1f9-1f1eb": { "fullName": "French Southern Territories", "shortName": "french-southern-territories" },
	"1f1f9-1f1ec": { "fullName": "Togo", "shortName": "togo" },
	"1f1f9-1f1ed": { "fullName": "Thailand", "shortName": "thailand" },
	"1f1f9-1f1ef": { "fullName": "Tajikistan", "shortName": "tajikistan" },
	"1f1f9-1f1f0": { "fullName": "Tokelau", "shortName": "tokelau" },
	"1f1f9-1f1f1": { "fullName": "Timor-Leste", "shortName": "timor-leste" },
	"1f1f9-1f1f2": { "fullName": "Turkmenistan", "shortName": "turkmenistan" },
	"1f1f9-1f1f3": { "fullName": "Tunisia", "shortName": "tunisia" },
	"1f1f9-1f1f4": { "fullName": "Tonga", "shortName": "tonga" },
	"1f1f9-1f1f7": { "fullName": "Turkey", "shortName": "turkey" },
	"1f1f9-1f1f9": { "fullName": "Trinidad & Tobago", "shortName": "trinidad-tobago" },
	"1f1f9-1f1fb": { "fullName": "Tuvalu", "shortName": "tuvalu" },
	"1f1f9-1f1fc": { "fullName": "Taiwan", "shortName": "taiwan" },
	"1f1f9-1f1ff": { "fullName": "Tanzania", "shortName": "tanzania" },
	"1f1fa-1f1e6": { "fullName": "Ukraine", "shortName": "ukraine" },
	"1f1fa-1f1ec": { "fullName": "Uganda", "shortName": "uganda" },
	"1f1fa-1f1f2": { "fullName": "U.S. Outlying Islands", "shortName": "us-outlying-islands" },
	"1f1fa-1f1f3": { "fullName": "United Nations", "shortName": "united-nations" },
	"1f1fa-1f1f8": { "fullName": "United States", "shortName": "united-states" },
	"1f1fa-1f1fe": { "fullName": "Uruguay", "shortName": "uruguay" },
	"1f1fa-1f1ff": { "fullName": "Uzbekistan", "shortName": "uzbekistan" },
	"1f1fb-1f1e6": { "fullName": "Vatican City", "shortName": "vatican-city" },
	"1f1fb-1f1e8": { "fullName": "St. Vincent & Grenadines", "shortName": "st-vincent-grenadines" },
	"1f1fb-1f1ea": { "fullName": "Venezuela", "shortName": "venezuela" },
	"1f1fb-1f1ec": { "fullName": "British Virgin Islands", "shortName": "british-virgin-islands" },
	"1f1fb-1f1ee": { "fullName": "U.S. Virgin Islands", "shortName": "us-virgin-islands" },
	"1f1fb-1f1f3": { "fullName": "Vietnam", "shortName": "vietnam" },
	"1f1fb-1f1fa": { "fullName": "Vanuatu", "shortName": "vanuatu" },
	"1f1fc-1f1eb": { "fullName": "Wallis & Futuna", "shortName": "wallis-futuna" },
	"1f1fc-1f1f8": { "fullName": "Samoa", "shortName": "samoa" },
	"1f1fd-1f1f0": { "fullName": "Kosovo", "shortName": "kosovo" },
	"1f1fe-1f1ea": { "fullName": "Yemen", "shortName": "yemen" },
	"1f1fe-1f1f9": { "fullName": "Mayotte", "shortName": "mayotte" },
	"1f1ff-1f1e6": { "fullName": "South Africa", "shortName": "south-africa" },
	"1f1ff-1f1f2": { "fullName": "Zambia", "shortName": "zambia" },
	"1f1ff-1f1fc": { "fullName": "Zimbabwe", "shortName": "zimbabwe" },

	"1f3f4-e0067-e0062-e0065-e006e-e0067-e007f": { "fullName": "England", "shortName": "england" },
	"1f3f4-e0067-e0062-e0073-e0063-e0074-e007f": { "fullName": "Scotland", "shortName": "scotland" },
	"1f3f4-e0067-e0062-e0077-e006c-e0073-e007f": { "fullName": "Wales", "shortName": "wales" }
};
urlNumbers = {
	"skype": "289",
	"lg": "307",
	"joypixels": "340"
};

# Using this instead of creating a new request everytime is like a 85x speedup
session = requests.Session()

# This is hilariously inefficient
for style, styleNum in urlNumbers.items():
	
	# Create directory for style if doesn't exist already
	style_path = os.path.join(flag_path, style)
	if not os.path.exists(style_path):
		os.makedirs(style_path)

	# Download every flag
	for chars, obj in flagNames.items():


		if style != "emojidex": req_url = url % (style, styleNum, obj["shortName"], chars)
		else: 					req_url = url % (style, styleNum, "for-"+obj["shortName"], chars)

		print(style, obj["fullName"], req_url)

		request = session.get(req_url)

		if "Access Denied" not in str(request.content):
			print("download!")
			with open(os.path.join(flag_path, style, f"{chars}.png"), "wb") as file:
				file.write(request.content)
