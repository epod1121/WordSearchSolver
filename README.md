# WordSearchSolver
This is my first time using webscraping in a coding project. This finds all of the letters, hints, and number of words, and feeds it to a local gemini to find the words.

This is a beginner project so I am well aware this isn't entirely useful. However, it was fun to get everything to word together to create somewhat of a decent output. It works by finding the words or elements by targeting the css selector (what makes the words have a font, color, etc in html). It then takes those elements, adds them to an array, then feeds it to a local gemini to try and unscramble it. The part that gives me the biggest headache is the response from the AI. It is able to find parts of some words but it overcomplicates it way too much.
