<template>
  <div class="container">
    <h1>Not Defterim</h1>
    <form @submit.prevent="addNote">
      <input
        v-model="newNote"
        type="text"
        placeholder="Yeni notunu yaz..."
        required
      />
      <button type="submit">Ekle</button>
    </form>

    <ul v-if="notes.length > 0">
      <li v-for="(note, index) in notes" :key="index">{{ note }}</li>
    </ul>
    <p v-else>Henüz not eklenmemiş.</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      newNote: '',
      notes: [],
    };
  },
  methods: {
    addNote() {
      if (this.newNote.trim() !== '') {
        this.notes.push(this.newNote.trim());
        this.newNote = '';
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 30px auto;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 0 8px rgba(0,0,0,0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
  text-align: center;
  color: #333;
}

form {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

input[type="text"] {
  flex-grow: 1;
  padding: 10px;
  border: 2px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

input[type="text"]:focus {
  border-color: #42b983;
  outline: none;
}

button {
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #369f6e;
}

ul {
  list-style-type: disc;
  padding-left: 20px;
  color: #555;
}
</style>
