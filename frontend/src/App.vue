<template>
  <div id="app">
    <router-view :sourceAvatar="sourceAvatar" :targetAvatar="targetAvatar" :loadHistory="loadHistory" />
  </div>
</template>

<script>
import BotIcon from './assets/bot.png'
import UsrIcon from './assets/bear.jpg'
export default {
  name: 'App',
  components: {
    BotIcon,
    UsrIcon,
  },
  data () {
    return {
      sourceAvatar: UsrIcon,
      targetAvatar: BotIcon
    }
  },
  methods: {
    // 定义加载历史消息的方式，该函数应该返回一个对象（`{ messages, hasMore }`），或者是返回该对象的 Promise （异步）。
    loadHistory () {
      return { 
        // 消息数据，字段如下，应以时间的倒序给出。
        messages: [
          { text: "Ask me any questions like what you will do to ChatGPT, come on!", time: new Date(), direction: 'received' },
          { text: "What can you do!", time: new Date(), direction: 'sent' },
          { text: "Hey, I'm a AI backended chatbot developed by Ryan LI, see 172.26.53.226:4000 for the development documentation!", time: new Date(), direction: 'received' },
          { text: 'Hello, who are you?', time: new Date(), direction: 'sent' },
        ], 
        // 定义是否还有历史消息，如果为 false，将停止加载。读者可将其改为 true 演示一下自动滚动更新的效果。
        hasMore: false 
      }
    },
  }
};
</script>

<style lang="scss" scoped>
#app {
  height: 1000px;
  padding-left: 200px;
  padding-right: 200px;
}
</style>
