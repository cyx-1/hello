import { createApp, ref } from 'vue';

// Vue Component using Composition API
const HelloWorld = {
  setup() {
    // Line 6: Reactive state using ref()
    const message = ref('Hello from Vue with TypeScript!');
    const count = ref(0);

    // Line 10: Method to increment counter
    const increment = () => {
      count.value++;
      console.log(`Count incremented to: ${count.value}`);
    };

    // Line 16: Expose reactive data and methods to template
    return {
      message,
      count,
      increment
    };
  },
  // Line 23: Template definition
  template: `
    <div class="container">
      <h1>{{ message }}</h1>
      <p>You clicked {{ count }} times</p>
      <button @click="increment">Click me</button>
    </div>
  `
};

// Line 33: Create and mount Vue app
const app = createApp(HelloWorld);
app.mount('#app');

console.log('Vue app mounted successfully!');
