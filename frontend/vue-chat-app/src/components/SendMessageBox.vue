<template>
  <div>
    <input type="text" v-model="inputValue" v-on:keyup.enter="submitMessage"/>
    <button v-on:click="submitMessage">Submit</button>
  </div>
</template>

<script>
import {store, SERVER_URL} from "@/App.vue";
import axios from "axios";

export default {
  name: 'SendMessageBox',
  computed: {
    inputValue: {
      set(val) {
        store.currentContent = val
      },
      get() {
        return store.currentContent
      }
    }
  },
  methods: {
    submitMessage: function () {
      if (!store.currentContent) {
        return
      }

      axios.post(SERVER_URL+ "/message", {
        "receiver_id": store.receiver_id,
        "sender_id": store.sender_id,
        "content": store.currentContent
      }).then(() => {
        //Because we use websocket to notify us of new messages, this becomes unnecessary
        // store.loadMessages()
      }).catch((error) => {
        console.log(error)
      })
      store.currentContent = "";
    }
  }
}
</script>

<style scoped>
div {
  display: grid;
  grid-template-columns: 10fr 2fr;
  background: color(srgb 0.0612 0.1472 0.3502);
  padding: 10px;
  padding-top: 0;;
}

input {
  background: rgb(240, 240, 240);
  padding: 8px;
  border-radius: 5px 0 0 5px;
  border: 0;
}

button {
  padding: 10px 20px;
  background: rgb(0, 92, 255);

  outline: 0;
  border: 0;
  color: white;
  border-radius: 0 5px 5px 0;
}

button:focus {
  outline: 0;
}
</style>