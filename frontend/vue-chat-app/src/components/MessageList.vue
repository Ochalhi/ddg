<template>
  <div id="list">
    <MessageBox v-for="message in getMessages()"
                :key="message.id"
                :sender_id="message.sender_id"
                :content="message.content"
                :timestamp="message.timestamp"/>
  </div>
</template>

<script>
import MessageBox from "@/components/MessageBox.vue";
import {store} from "@/App.vue";

export default {
  name: 'MessageList',
  components: {MessageBox},
  updated() {
    let container = document.getElementById("list");
    container.scrollTop = container.scrollHeight
  },
  beforeCreate() {
    store.loadMessages()
  },
  methods:{
    getMessages(){
      return store.messages;
    }
  }
}


</script>

<style scoped>
#list{
  overflow-y: scroll;
  background: color(srgb 0 0.0538 0.15);
}
</style>