### 01 Exercise - Templates
This is a set of exercises to finish in week 1 of the semester on setting up multiple different Flask projects.
In all cases, use the proper project structure as given in the lectures and slide decks. You should get the project set up and working in pycharm-community.

Learn to get the skeleton of the app correct and working as quickly and efficiently as possible so that you can focus on the core part of the programming with minimal delay. Your aim is to get to the point where putting a skeleton of an app and getting it working in Pycharm is extremely quick and easy.

Make hte following Flask apps (each one is a different project, but you can copy files or code snippets from handout materials and your previous exercises):

1. Show the date and time of day when the user lands on the home page of the app
2. Show a random quote from a list of quotes. You can find a suitable list of quotes from, for example, https://gist.github.com/robatron/a66acc0eed3835119817 or find an alternative list on the web. The list of quotes can be embedded in the source code of the app.
    * To extend this app, modify it so that you read the list of quotes from a file in the static folder of the app when the application starts up.
3. Write an app that uses a dynamic route ending with a positive integer and generates a page that shows the prime divisors of the integer (which may be just 1 and the integer itself if it is prime). You can use code from the web for primality testing (c.f. [Primality_test](https://en.wikipedia.org/wiki/Primality_test))
4. Write an app that shows values from the App object on one page and the Request object on another.
   * Extend this app by adding a navigation bar using template inheritance to simplify switching between pages.
5. Write an app that combines all the above apps with a navigation bar that can switch between all the pages.