import os
import requests

path = os.path.dirname(os.path.abspath(__file__))
flag_path = os.path.join(path, "src", "flags")

flagNames = [
	"1f1e6-1f1e8",
	"1f1e6-1f1e9",
	"1f1e6-1f1ea",
	"1f1e6-1f1eb",
	"1f1e6-1f1ec",
	"1f1e6-1f1ee",
	"1f1e6-1f1f1",
	"1f1e6-1f1f2",
	"1f1e6-1f1f4",
	"1f1e6-1f1f6",
	"1f1e6-1f1f7",
	"1f1e6-1f1f8",
	"1f1e6-1f1f9",
	"1f1e6-1f1fa",
	"1f1e6-1f1fc",
	"1f1e6-1f1fd",
	"1f1e6-1f1ff",
	"1f1e7-1f1e6",
	"1f1e7-1f1e7",
	"1f1e7-1f1e9",
	"1f1e7-1f1ea",
	"1f1e7-1f1eb",
	"1f1e7-1f1ec",
	"1f1e7-1f1ed",
	"1f1e7-1f1ee",
	"1f1e7-1f1ef",
	"1f1e7-1f1f1",
	"1f1e7-1f1f2",
	"1f1e7-1f1f3",
	"1f1e7-1f1f4",
	"1f1e7-1f1f6",
	"1f1e7-1f1f7",
	"1f1e7-1f1f8",
	"1f1e7-1f1f9",
	"1f1e7-1f1fb",
	"1f1e7-1f1fc",
	"1f1e7-1f1fe",
	"1f1e7-1f1ff",
	"1f1e8-1f1e6",
	"1f1e8-1f1e8",
	"1f1e8-1f1e9",
	"1f1e8-1f1eb",
	"1f1e8-1f1ec",
	"1f1e8-1f1ed",
	"1f1e8-1f1ee",
	"1f1e8-1f1f0",
	"1f1e8-1f1f1",
	"1f1e8-1f1f2",
	"1f1e8-1f1f3",
	"1f1e8-1f1f4",
	"1f1e8-1f1f5",
	"1f1e8-1f1f7",
	"1f1e8-1f1fa",
	"1f1e8-1f1fb",
	"1f1e8-1f1fc",
	"1f1e8-1f1fd",
	"1f1e8-1f1fe",
	"1f1e8-1f1ff",
	"1f1e9-1f1ea",
	"1f1e9-1f1ec",
	"1f1e9-1f1ef",
	"1f1e9-1f1f0",
	"1f1e9-1f1f2",
	"1f1e9-1f1f4",
	"1f1e9-1f1ff",
	"1f1ea-1f1e6",
	"1f1ea-1f1e8",
	"1f1ea-1f1ea",
	"1f1ea-1f1ec",
	"1f1ea-1f1ed",
	"1f1ea-1f1f7",
	"1f1ea-1f1f8",
	"1f1ea-1f1f9",
	"1f1ea-1f1fa",
	"1f1eb-1f1ee",
	"1f1eb-1f1ef",
	"1f1eb-1f1f0",
	"1f1eb-1f1f2",
	"1f1eb-1f1f4",
	"1f1eb-1f1f7",
	"1f1ec-1f1e6",
	"1f1ec-1f1e7",
	"1f1ec-1f1e9",
	"1f1ec-1f1ea",
	"1f1ec-1f1eb",
	"1f1ec-1f1ec",
	"1f1ec-1f1ed",
	"1f1ec-1f1ee",
	"1f1ec-1f1f1",
	"1f1ec-1f1f2",
	"1f1ec-1f1f3",
	"1f1ec-1f1f5",
	"1f1ec-1f1f6",
	"1f1ec-1f1f7",
	"1f1ec-1f1f8",
	"1f1ec-1f1f9",
	"1f1ec-1f1fa",
	"1f1ec-1f1fc",
	"1f1ec-1f1fe",
	"1f1ed-1f1f0",
	"1f1ed-1f1f2",
	"1f1ed-1f1f3",
	"1f1ed-1f1f7",
	"1f1ed-1f1f9",
	"1f1ed-1f1fa",
	"1f1ee-1f1e8",
	"1f1ee-1f1e9",
	"1f1ee-1f1ea",
	"1f1ee-1f1f1",
	"1f1ee-1f1f2",
	"1f1ee-1f1f3",
	"1f1ee-1f1f4",
	"1f1ee-1f1f6",
	"1f1ee-1f1f7",
	"1f1ee-1f1f8",
	"1f1ee-1f1f9",
	"1f1ef-1f1ea",
	"1f1ef-1f1f2",
	"1f1ef-1f1f4",
	"1f1ef-1f1f5",
	"1f1f0-1f1ea",
	"1f1f0-1f1ec",
	"1f1f0-1f1ed",
	"1f1f0-1f1ee",
	"1f1f0-1f1f2",
	"1f1f0-1f1f3",
	"1f1f0-1f1f5",
	"1f1f0-1f1f7",
	"1f1f0-1f1fc",
	"1f1f0-1f1fe",
	"1f1f0-1f1ff",
	"1f1f1-1f1e6",
	"1f1f1-1f1e7",
	"1f1f1-1f1e8",
	"1f1f1-1f1ee",
	"1f1f1-1f1f0",
	"1f1f1-1f1f7",
	"1f1f1-1f1f8",
	"1f1f1-1f1f9",
	"1f1f1-1f1fa",
	"1f1f1-1f1fb",
	"1f1f1-1f1fe",
	"1f1f2-1f1e6",
	"1f1f2-1f1e8",
	"1f1f2-1f1e9",
	"1f1f2-1f1ea",
	"1f1f2-1f1eb",
	"1f1f2-1f1ec",
	"1f1f2-1f1ed",
	"1f1f2-1f1f0",
	"1f1f2-1f1f1",
	"1f1f2-1f1f2",
	"1f1f2-1f1f3",
	"1f1f2-1f1f4",
	"1f1f2-1f1f5",
	"1f1f2-1f1f6",
	"1f1f2-1f1f7",
	"1f1f2-1f1f8",
	"1f1f2-1f1f9",
	"1f1f2-1f1fa",
	"1f1f2-1f1fb",
	"1f1f2-1f1fc",
	"1f1f2-1f1fd",
	"1f1f2-1f1fe",
	"1f1f2-1f1ff",
	"1f1f3-1f1e6",
	"1f1f3-1f1e8",
	"1f1f3-1f1ea",
	"1f1f3-1f1eb",
	"1f1f3-1f1ec",
	"1f1f3-1f1ee",
	"1f1f3-1f1f1",
	"1f1f3-1f1f4",
	"1f1f3-1f1f5",
	"1f1f3-1f1f7",
	"1f1f3-1f1fa",
	"1f1f3-1f1ff",
	"1f1f4-1f1f2",
	"1f1f5-1f1e6",
	"1f1f5-1f1ea",
	"1f1f5-1f1eb",
	"1f1f5-1f1ec",
	"1f1f5-1f1ed",
	"1f1f5-1f1f0",
	"1f1f5-1f1f1",
	"1f1f5-1f1f2",
	"1f1f5-1f1f3",
	"1f1f5-1f1f7",
	"1f1f5-1f1f8",
	"1f1f5-1f1f9",
	"1f1f5-1f1fc",
	"1f1f5-1f1fe",
	"1f1f6-1f1e6",
	"1f1f7-1f1ea",
	"1f1f7-1f1f4",
	"1f1f7-1f1f8",
	"1f1f7-1f1fa",
	"1f1f7-1f1fc",
	"1f1f8-1f1e6",
	"1f1f8-1f1e7",
	"1f1f8-1f1e8",
	"1f1f8-1f1e9",
	"1f1f8-1f1ea",
	"1f1f8-1f1ec",
	"1f1f8-1f1ed",
	"1f1f8-1f1ee",
	"1f1f8-1f1ef",
	"1f1f8-1f1f0",
	"1f1f8-1f1f1",
	"1f1f8-1f1f2",
	"1f1f8-1f1f3",
	"1f1f8-1f1f4",
	"1f1f8-1f1f7",
	"1f1f8-1f1f8",
	"1f1f8-1f1f9",
	"1f1f8-1f1fb",
	"1f1f8-1f1fd",
	"1f1f8-1f1fe",
	"1f1f8-1f1ff",
	"1f1f9-1f1e6",
	"1f1f9-1f1e8",
	"1f1f9-1f1e9",
	"1f1f9-1f1eb",
	"1f1f9-1f1ec",
	"1f1f9-1f1ed",
	"1f1f9-1f1ef",
	"1f1f9-1f1f0",
	"1f1f9-1f1f1",
	"1f1f9-1f1f2",
	"1f1f9-1f1f3",
	"1f1f9-1f1f4",
	"1f1f9-1f1f7",
	"1f1f9-1f1f9",
	"1f1f9-1f1fb",
	"1f1f9-1f1fc",
	"1f1f9-1f1ff",
	"1f1fa-1f1e6",
	"1f1fa-1f1ec",
	"1f1fa-1f1f2",
	"1f1fa-1f1f3",
	"1f1fa-1f1f8",
	"1f1fa-1f1fe",
	"1f1fa-1f1ff",
	"1f1fb-1f1e6",
	"1f1fb-1f1e8",
	"1f1fb-1f1ea",
	"1f1fb-1f1ec",
	"1f1fb-1f1ee",
	"1f1fb-1f1f3",
	"1f1fb-1f1fa",
	"1f1fc-1f1eb",
	"1f1fc-1f1f8",
	"1f1fd-1f1f0",
	"1f1fe-1f1ea",
	"1f1fe-1f1f9",
	"1f1ff-1f1e6",
	"1f1ff-1f1f2",
	"1f1ff-1f1fc",

	"1f3f4-e0067-e0062-e0065-e006e-e0067-e007f",
	"1f3f4-e0067-e0062-e0073-e0063-e0074-e007f",
	"1f3f4-e0067-e0062-e0077-e006c-e0073-e007f",
	"1f3f4-e0064-e0065-e0062-e0079-e007f",
	"1f3f4-e0064-e0065-e0062-e0065-e007f",
	"1f3f4-e0065-e0073-e0061-e0073-e007f",
	"1f3f4-e0065-e0073-e0070-e0076-e007f",
	"1f3f4-e0065-e0073-e0063-e0074-e007f",
	"1f3f4-e0066-e0072-e0062-e0072-e0065-e007f",
	"1f3f4-e0063-e0061-e0071-e0063-e007f",
	"1f3f4-e0075-e0073-e0063-e0061-e007f",
	"1f3f4-e0075-e0073-e0074-e0078-e007f",
]

session = requests.Session()

urls = {
	# "twitter": "https://abs-0.twimg.com/emoji/v2/svg/%s.svg",
	# "openmoji": "https://openmoji.org/data/color/svg/%s.svg",
	"joypixels": "https://cdn.joypixels.com/emoji/joypixels/8.0/png/unicode/128/%s.png"
}

# Download every flag
for styleName, url in urls.items():

	# Create directory for style if doesn't exist already
	style_path = os.path.join(flag_path, styleName)
	if not os.path.exists(style_path):
		os.makedirs(style_path)

	file_type = url.split(".")[-1]

	for chars in flagNames:

		if styleName == "openmoji": chars = chars.upper()

		req_url = url % chars
		print(styleName, chars, req_url)

		request = session.get(req_url)

		if "Access Denied" not in str(request.content):
			with open(os.path.join(style_path, f"{chars}.{file_type}"), "wb") as file:
				file.write(request.content)
