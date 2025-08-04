<template>
  <div class="note-form">
    <h2>Add a Note</h2>
    <form @submit.prevent="submitNote">
      <input v-model="title" placeholder="Note title" required />
      <textarea v-model="content" placeholder="Note content" required></textarea>
      <input v-model="username" placeholder="Your username" required />
      <button type="submit">Submit</button>
    </form>

    <div v-if="message" class="message">{{ message }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      content: '',
      username: '',
      message: ''
    };
  },
  methods: {
    async submitNote() {
      try {
        const response = await fetch('http://localhost:8000/api/create-note/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            title: this.title,
            content: this.content,
            username: this.username
          })
        });

        const data = await response.json();
        if (response.ok) {
          this.message = 'Note added successfully!';
          this.title = '';
          this.content = '';
        } else {
          this.message = 'Error: ' + data.error;
        }
      } catch (err) {
        this.message = 'Fetch error: ' + err.message;
      }
    }
  }
};
</script>

<style scoped>
.note-form {
  max-width: 500px;
  margin: auto;
  padding: 1rem;
}
textarea {
  width: 100%;
  height: 100px;
  margin-top: 10px;
}
.message {
  margin-top: 1rem;
  color: green;
}
</style>
