# console_bot
 <h2>Simple console bot</h2>
<p>This bot is a simple contact manager that allows you to store and retrieve contact information using various commands. It runs in the console and responds to user input.</p>

<h2>Bot Instructions</h2>
<p>This bot accepts the following commands:</p>
<ul>
  <li><code>hello</code>: Responds with "How can I help you?"</li>
  <li><code>add ...</code>: Stores a new contact in memory (e.g., in a dictionary). Replace the ellipsis (...) with the name and phone number separated by a space.</li>
  <li><code>change ...</code>: Updates the phone number of an existing contact in memory. Replace the ellipsis (...) with the name and the new phone number separated by a space.</li>
  <li><code>phone ...</code>: Displays the phone number of the specified contact in the console. Replace the ellipsis (...) with the contact name.</li>
  <li><code>show all</code>: Prints all saved contacts with their phone numbers in the console.</li>
  <li><code>good bye</code>, <code>close</code>, <code>exit</code>: Terminates the bot's execution after displaying "Good bye!" in the console.</li>
</ul>

<h2>Input Error Handling</h2>
<p>The bot handles user input errors using the input_error decorator. This decorator catches exceptions (such as KeyError, ValueError, and IndexError) that may occur in the handler functions and returns appropriate error messages to the user. Examples of error messages include "Enter user name" and "Give me name and phone please."</p>
