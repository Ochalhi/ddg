<template>
  <ChatBox/>
</template>

<script>
import ChatBox from './components/ChatBox.vue'
import {reactive} from 'vue';
import axios from "axios";
import {io} from "socket.io-client";
export const SERVER_URL = process.env.NODE_ENV === "production" ? undefined : "http://localhost:8000";

export const socket = io(SERVER_URL);

socket.on("connect", () => {
  console.log("connected");
});

socket.on("disconnect", () => {
  console.log("disconnected");
});

socket.on("new-message", (message) => {
  console.log("new message bro")
  store.messages.push(message);
});

export default {
  name: 'App',
  components: {
    ChatBox
  }
}

export const store = reactive({
  sender_id: 1,
  receiver_id: 2,
  currentContent: '',
  messages: [],
  loadMessages() {
    axios.get(SERVER_URL+"/message",
        {
          params: {
            "receiver_id": store.receiver_id,
            "sender_id": store.sender_id,
          }
        }).then(res => {
      if (res.status === 200) {
        console.log(res.data)
        store.messages = res.data.sort((a, b) => a.id - b.id)
      }
    }).catch(res => {
      console.log("Error retrieving data:" + res)
    })
  },
})

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background: black;
  display: grid;
  grid-template-rows: 1fr;
  height: 100vh;
}

body {
  background: black;
  margin: 0;
  max-height: 100vh;
  height: 100vh;
  display: grid;
  font-size: 14px;
}
button:hover{
  cursor: pointer;
}
</style>
