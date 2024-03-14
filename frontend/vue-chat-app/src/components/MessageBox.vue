<script>
export default {
  name: "MessageBox", props: [
    'sender_id',
    'content',
    'timestamp'
  ],
  computed: {
    getUserColorClass() {
      return "user" + this.sender_id;
    }
  }
}
</script>

<template>
  <div class="messageBox">
    <p>
      <span v-bind:class="getUserColorClass">User {{ sender_id }}: </span>
      <span>{{ content }}</span>
    </p>
    <p class="timestamp">{{ timestamp }}</p>
  </div>
</template>


<style scoped>
.timestamp {
  color: rgb(116, 162, 246);
  font-size: 11px;
}

.user1 {
  color: color(srgb 1 0.425 0.997);
  font-weight: bold;

}

.user2 {
  color: color(srgb 1 0.6839 0);
  font-weight: bold;
}

div {
  background: rgb(15, 38, 89);
  margin: 20px;
  text-align: left;
  border-radius: 5px;
  padding: 10px 15px;
}

p {
  margin: 0;
}
</style>