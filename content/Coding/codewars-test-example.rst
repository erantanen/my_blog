Codewars test example
#####################
:date: 2014-05-30 00:47
:author: Ed Rantanen
:category: coding
:slug: codewars-test-example
:status: published

| A couple of weeks ago a friend sent me a something to checkout,
  `Codewars <http://www.codewars.com>`__, after poking around a bit I
  thought it was pretty cool! And I did the first couple of bits in
  javascript (looking forward to when they implement c) but after that
  did not get any further. Seems I ran into a little wall, the test
  cases. Initially on the site the documentation kinda describes what is
  required to complete the test cases, once again the "clueless bug" hit
  me.
| My friend Google came to the rescue a few minutes of searches the
  example for `test.expect <https://gist.github.com/sathvikp/6199815>`__
  was found!
| Sent a thank you to the author.

| This is what you initially see on the Codewars site for tests.
| `` //Create your own tests here. These are some of the methods available: // Test.expect(boolean, [optional] message) // Test.assertEquals(actual, expected, [optional] message) // Test.assertSimilar(actual, expected, [optional] message) // Test.assertNotEquals(actual, expected, [optional] message)``

| And this was the example I found.
| ``var input = "The quick brown fox jumped over the lazy developer."; var expectedResult ="The quick brown fox jump-\ned over the lazy develop-\ner."; var result = wordWrap(input); Test.expect(result === expectedResult);``

| I made a simple function to turn a number into a string.
| `` function numToString(num){ var token = num.toString(); return token; }``
| And yes I could have made it smaller, so the test case looked like
  this.

| ``var input = 5; var expectedResult = "5"; var result = numToString(input); Test.expect(result === expectedResult);``
| And Wooo Weee it worked!

It is only one test of the lot, but now I have clear idea on what is
needed.
