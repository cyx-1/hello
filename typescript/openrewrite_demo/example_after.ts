/**
 * Example TypeScript Code AFTER OpenRewrite Transformation
 *
 * This file shows the same code after OpenRewrite has applied
 * modern TypeScript best practices.
 */

// ✅ Improvement 1: Using 'let' and 'const' instead of 'var'
let globalCounter = 0;
const applicationName = "MyApp";

function processData() {
    const items = [1, 2, 3, 4, 5];
    let total = 0;

    for (let i = 0; i < items.length; i++) {
        total += items[i];
    }

    return total;
}

// ✅ Improvement 2: Template literals instead of string concatenation
function getUserGreeting(firstName: string, lastName: string, age: number) {
    const greeting = `Hello, ${firstName} ${lastName}!`;
    const info = `You are ${age} years old.`;
    const fullMessage = `${greeting} ${info}`;

    return fullMessage;
}

// ✅ Improvement 3: Arrow functions
const multiply = (a: number, b: number) => a * b;

const filterEvenNumbers = (numbers: number[]) =>
    numbers.filter(n => n % 2 === 0);

// ✅ Improvement 4: Async/await instead of promise chains
async function fetchUserProfile(userId: string) {
    try {
        const response = await fetch(`/api/user/${userId}`);
        const user = await response.json();

        const postsResponse = await fetch(`/api/posts/${user.id}`);
        const posts = await postsResponse.json();

        console.log(`User has ${posts.length} posts`);
        return posts;
    } catch (error) {
        console.error(`Error: ${(error as Error).message}`);
        throw error;
    }
}

// ✅ Improvement 5: Optional chaining
function getUsername(user: any) {
    return user?.profile?.name ?? 'Anonymous';
}

// ✅ Improvement 6: ES6 exports
export {
    processData,
    getUserGreeting,
    multiply,
    filterEvenNumbers,
    fetchUserProfile,
    getUsername
};

console.log("This file demonstrates modernized code after OpenRewrite transformation");
