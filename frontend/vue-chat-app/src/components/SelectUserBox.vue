<script>
import {store} from "@/App.vue";

export default {
  name: 'SelectUserBox',
  props: [
    'selectedUser'
  ],
  methods: {
    selected(id) {
      return store.sender_id === id ? "selected" : "";
    },
    select(senderId, receiverId) {
      store.sender_id = senderId;
      store.receiver_id = receiverId;
      store.loadMessages()
    }
  }
}
</script>

<template>
  <div>
    <button v-bind:class="selected(1)" v-on:click="select(1,2)">
      User 1
    </button>
    <div id="seperator"></div>
    <button v-bind:class="selected(2)" v-on:click="select(2,1)">
      User 2
    </button>
  </div>
</template>

<style scoped>
.selected {
  background: rgb(0, 92, 255);
}

div {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  background: color(srgb 0.0612 0.1472 0.3502);
  padding: 10px;
}

input {
  background: rgb(240, 240, 240);
  padding: 8px;
  width: 500px;
}
#seperator{
  width: 10px;
  padding: 0;
}
button {
  padding: 10px 20px;
  background: rgb(16, 69, 162);
  outline: 0;
  border: 0;
  color: white;
  border-radius: 5px;
}

</style>