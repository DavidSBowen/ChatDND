<template>
    <form @submit.prevent="onSubmit">
      <input v-model="value" />
  
      <button type="submit" :disabled="isLoading">Submit</button>
    </form>
  </template>
  
  <script>
  import { socket } from "@/socket";
  
  export default {
    name: "MyForm",
  
    data() {
      return {
        isLoading: false,
        value: ""
      }
    },
  
    methods: {
      onSubmit() {
        this.isLoading = true;
  
        socket.timeout(5000).emit("create-something", this.value, () => {
          this.isLoading = false;
        });
      },
    }
  }
  </script>