/**
 * Example TypeScript Code BEFORE OpenRewrite Transformation
 *
 * This file contains various anti-patterns and outdated syntax
 * that OpenRewrite can automatically refactor.
 */

// Anti-pattern 1: Using 'var' instead of 'let' or 'const'
var globalCounter = 0;
var applicationName = "MyApp";

function processData() {
    var items = [1, 2, 3, 4, 5];
    var total = 0;

    for (var i = 0; i < items.length; i++) {
        total += items[i];
    }

    return total;
}

// Anti-pattern 2: String concatenation instead of template literals
function getUserGreeting(firstName, lastName, age) {
    var greeting = "Hello, " + firstName + " " + lastName + "!";
    var info = "You are " + age + " years old.";
    var fullMessage = greeting + " " + info;

    return fullMessage;
}

// Anti-pattern 3: Traditional function expressions
var multiply = function(a, b) {
    return a * b;
};

var filterEvenNumbers = function(numbers) {
    return numbers.filter(function(n) {
        return n % 2 === 0;
    });
};

// Anti-pattern 4: Promise chains instead of async/await
function fetchUserProfile(userId) {
    return fetch('/api/user/' + userId)
        .then(function(response) {
            return response.json();
        })
        .then(function(user) {
            return fetch('/api/posts/' + user.id);
        })
        .then(function(postsResponse) {
            return postsResponse.json();
        })
        .then(function(posts) {
            console.log('User has ' + posts.length + ' posts');
            return posts;
        })
        .catch(function(error) {
            console.error('Error: ' + error.message);
            throw error;
        });
}

// Anti-pattern 5: Verbose null checks
function getUsername(user) {
    if (user && user.profile && user.profile.name) {
        return user.profile.name;
    }
    return 'Anonymous';
}

// Anti-pattern 6: CommonJS exports (simulated)
// module.exports = {
//     processData: processData,
//     getUserGreeting: getUserGreeting,
//     multiply: multiply
// };

console.log("This file demonstrates code patterns that OpenRewrite can modernize");
