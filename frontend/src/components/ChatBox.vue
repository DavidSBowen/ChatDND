<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12" v-for="message in messages" :key="message.id">
        <div class="row mb-2" :class="{ 'justify-content-end': message.isMe }">
          <div class="col-md-6 p-2" :class="{ 'bg-primary text-white': message.isMe, 'bg-light': !message.isMe }">
            <span>{{ message.content }}</span>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <div class="input-group">
          <input v-model="inputText" type="text" class="form-control" placeholder="Type your message here..." @keydown.enter="sendMessage" />
          <div class="input-group-append">
            <button class="btn btn-primary" type="button" @click="sendMessage">Send</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputText: '',
      messages: [],
      messageId: 0,
      isMe: true,
    };
  },
  methods: {
    sendMessage() {
      if (this.inputText !== '') {
        this.messages.push({
          id: this.messageId++,
          content: this.inputText,
          isMe: this.isMe,
        });
        this.inputText = '';
        this.isMe = !this.isMe;
      }
    },
  },
};
</script>

<style>
</style>
