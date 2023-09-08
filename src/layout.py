"""
# Project: View MD
# Description: View MD is a simple tool to view markdown files in windows.
# Version: 1.0.0
# Version Code: 1
# Since: 1.0.0
# Author: Md. Ashraful Alam Shemul
# Email: ceo@stechbd.net
# Website: https://www.stechbd.net/project/View-MD/
# Developer: S Technologies
# Homepage: https://www.stechbd.net
# Contact: product@stechbd.net
# Created: August 8, 2023
# Updated: September 8, 2023
"""


def layout(file_name, content):
	template = '''<style>
	body {
		display: grid;
	}

	main {
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
		background-color: white;
		margin: 20px;
		border: 1px solid #D0D7DE;
		border-radius: 10px;
		/*box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);*/
	}

	main .title {
		border-bottom: 1px solid #D0D7DE;
		padding: 10px 30px;
	}

	main .title * {
		margin-right: 5px;
	}

	main .content {
		padding: 0 30px 10px 30px;
	}

	main > .content h1, main > .content h2, main > .content h3, main > .content h4, main > .content h5, main > .content h6 {
		border-bottom: 1px solid #D0D7DE;
		padding-bottom: 10px;
		margin-top: 30px;
	}

	main > .content a:link, main > .content a:visited {
		color: #218BFF;
		text-decoration: none;
	}

	main > .content a:hover {
		text-decoration: underline;
	}

	main > .content pre {
		background-color: #F6F8FA;
		padding: 20px;
		border-radius: 5px;
	}

	@media only-screen and (min-width: 768px) {
		aside {
			display: block;
		}
	}
</style>

<main>
	<div class="title">
		<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-markdown" viewBox="0 0 16 16">
			<path d="M14 3a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h12zM2 2a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H2z"/>
			<path fill-rule="evenodd" d="M9.146 8.146a.5.5 0 0 1 .708 0L11.5 9.793l1.646-1.647a.5.5 0 0 1 .708.708l-2 2a.5.5 0 0 1-.708 0l-2-2a.5.5 0 0 1 0-.708z"/>
			<path fill-rule="evenodd" d="M11.5 5a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-1 0v-4a.5.5 0 0 1 .5-.5z"/>
			<path d="M3.56 11V7.01h.056l1.428 3.239h.774l1.42-3.24h.056V11h1.073V5.001h-1.2l-1.71 3.894h-.039l-1.71-3.894H2.5V11h1.06z"/>
		</svg>
		<span><strong>''' + file_name + ''''</strong></span>
	</div>
	<div class="content">
		''' + content + '''
	</div>
</main>'''
	return template
