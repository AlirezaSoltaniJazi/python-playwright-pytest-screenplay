# Playwright with Screenplay Pattern (Python and pytest)

## Playwright

**Playwright** enables reliable end-to-end testing for modern web apps.

* Cross-browser. Playwright supports all modern rendering engines including Chromium, WebKit, and Firefox.
* Cross-platform. Test on Windows, Linux, and macOS, locally or on CI, headless or headed.
* Cross-language. Use the Playwright API in TypeScript, JavaScript, Python, .NET, Java.
* Test Mobile Web. Native mobile emulation of Google Chrome for Android and Mobile Safari. The same rendering engine
  works on your Desktop and in the Cloud.
* Auto-wait. Playwright waits for elements to be actionable prior to performing actions. It also has a rich set of
  introspection events. The combination of the two eliminates the need for artificial timeouts - the primary cause of
  flaky tests.
* Web-first assertions. Playwright assertions are created specifically for the dynamic web. Checks are automatically
  retried until the necessary conditions are met.
* Tracing. Configure test retry strategy, capture execution trace, videos, screenshots to eliminate flakes.
* Browsers run web content belonging to different origins in different processes. Playwright is aligned with the modern
  browsers architecture and runs tests out-of-process. This makes Playwright free of the typical in-process test runner
  limitations. Multiple everything. Test scenarios that span multiple tabs, multiple origins and multiple users. Create
  scenarios with different contexts for different users and run them against your server, all in one test.
* Trusted events. Hover elements, interact with dynamic controls, produce trusted events. Playwright uses real browser
  input pipeline indistinguishable from the real user. Test frames, pierce Shadow DOM. Playwright selectors pierce
  shadow DOM and allow entering frames seamlessly.
* Browser contexts. Playwright creates a browser context for each test. Browser context is equivalent to a brand new
  browser profile. This delivers full test isolation with zero overhead. Creating a new browser context only takes a
  handful of milliseconds.
* Log in once. Save the authentication state of the context and reuse it in all the tests. This bypasses repetitive
  log-in operations in each test, yet delivers full isolation of independent tests.
* Codegen. Generate tests by recording your actions. Save them into any language.
* Playwright inspector. Inspect page, generate selectors, step through the test execution, see click points, explore
  execution logs.
* Trace Viewer. Capture all the information to investigate the test failure. Playwright trace contains test execution
  screencast, live DOM snapshots, action explorer, test source, and many more.

## Screenplay Pattern

[Screenplay Pattern Doc](./screenplay_pattern.md)

## Development

[Development Doc](./development.md)

## Project Detail

Actor: User

Task: Search for a word on DuckDuckGo

Actions:

* Open DuckDuckGo search page
* Enter the word in the search bar
* Click the search button
  Questions:

* Are there any search results?
* Do the search results contain the word?
* Is the search input text the same as the word?
* Does the page title start with the word?
  Abilities:

* Navigate to a web page
* Enter text in a field
* Click a button
* Get the text of a link
* Get the text of an input field
* Get the title of a page

## Mapping

Mapping the code to these elements:

Actor:

* The user is represented by the page fixture.
  Task:
* The task of searching for a word on DuckDuckGo is implemented in the test_duck_duck_go_search() function.

Actions:

* The action of opening the DuckDuckGo search page is implemented by calling the load_search_page() method on the
  DuckDuckGoSearchPage object.
* The action of entering the word in the search bar is implemented by calling the fill() method on the search input
  field element.
* The action of clicking the search button is implemented by calling the click() method on the search input button
  element.

Questions:

* Whether there are any search results is implemented by checking the length of the list of search
  result links.
* Whether the search results contain the word is implemented by checking if the word is present in any
  of the search result titles.
* Whether the search input text is the same as the word is implemented by comparing the text of the
  search input field to the word.
* Whether the page title starts with the word is implemented by checking if the word is the prefix of
  the page title.

Abilities:

* The ability to navigate to a web page is implemented by the goto() method on the Page object.
* The ability to enter text in a field is implemented by the fill() method on the field element.
* The ability to click a button is implemented by the click() method on the button element.
* The ability to get the text of a link is implemented by the all_text_contents() method on the link element.
* The ability to get the text of an input field is implemented by the input_value() method on the input field element.
* The ability to get the title of a page is implemented by the title() method on the Page object.

## Step to Create Project
1. Create actor
2. Create ability
3.
