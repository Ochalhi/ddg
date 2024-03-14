<template>
  <div id="chatbox">
    <MessageList/>
    <SelectUserBox/>
    <SendMessageBox/>
  </div>
</template>

<script>
import SendMessageBox from "@/components/SendMessageBox.vue";
import SelectUserBox from "@/components/SelectUserBox.vue";
import MessageList from "@/components/MessageList.vue";

export default {
  name: 'ChatBox',
  components: {SelectUserBox, SendMessageBox, MessageList}
}

</script>

<style scoped>
#chatbox {
  color: white;
  background: black;
  display: grid;
  grid-template-rows: 1fr auto auto;
  padding: 50px;
  overflow: auto;

}
</style>