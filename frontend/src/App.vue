<template>
  <el-container height="10vh" >
  <el-header>
    <div>
      <span><img src="./assets/panda-bear.png" alt="" height="40px"/></span>
        <span>Chatbot</span>
    </div>
    <el-button type="info" @click="setting">Setting</el-button>
  </el-header>
  <el-container>
  <el-aside width="15%">
      <el-menu default-active="1" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b" >
        <el-menu-item index="1">
          <i class="el-icon-document"></i>
          <span slot="title">7B</span>
        </el-menu-item>
        <el-menu-item index="2" disabled>
          <i class="el-icon-document"></i>
          <span slot="title">13B</span>
        </el-menu-item>
        <el-menu-item index="3" disabled>
          <i class="el-icon-document" ></i>
          <span slot="title">33B</span>
        </el-menu-item>
        <el-menu-item index="3" disabled>
          <i class="el-icon-document" ></i>
          <span slot="title">65B</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
  <el-main>
  <div id="app">
    <router-view :sourceAvatar="sourceAvatar" :targetAvatar="targetAvatar" :loadHistory="loadHistory" />
  </div>
  </el-main>
  </el-container>
  </el-container>
</template>

<script>
import BotIcon from './assets/bot.png'
import UsrIcon from './assets/bear.png'
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
          { text: "- Do not prompt with \"Ten easy steps to build a website...\" but with \"Building a website can be done in 10 simple steps:\"\n- Do not prompt with \"What is the meaning of life? Be concise and do not repeat yourself.\" but with \"I believe the meaning of life is\" \n- Do not prompt with \"Explain the theory of relativity.\" but with \"Simply put, the theory of relativity states that\"", time: new Date(), direction: 'received' },
          { text: "Any notes before I start?", time: new Date(), direction: 'sent' },
          { text: "Ask me any questions like what you will do to ChatGPT, come on!", time: new Date(), direction: 'received' },
          { text: "What can you do!", time: new Date(), direction: 'sent' },
          { text: "Hey, I'm a AI backended chatbot developed by Ryan LI, see 172.26.53.226:4000 for the development documentation!", time: new Date(), direction: 'received' },
          { text: 'Hello, who are you?', time: new Date(), direction: 'sent' },
        ], 
        // 定义是否还有历史消息，如果为 false，将停止加载。读者可将其改为 true 演示一下自动滚动更新的效果。
        hasMore: false 
      }
    },
    setting() {

    }
  }
};
</script>

<style lang="scss" scoped>
#app {
  height: 90vh;
  padding-left: 10%;
  padding-right: 10%;
}
.el-header{
     background-color: #373d41;
     display: flex; //设置显示为flex布局
     justify-content: space-between;//设置为flex左右布局
     padding-left: 0;//左内边距为0（Logo贴左边）
     align-items: center;//元素上下居中（防止右边按钮贴上下边）
     color: #fff;
     font-size: 15px;
     > div {//内嵌的div样式
         display: flex;
         align-items: center;//Logo和文字上下居中
         span {
             margin-left: 15px;//文字左侧设置间距，防止与Logo紧贴
         }
     }
    }


.el-aside {
  background-color: #333744;
}
.el-main {
  background-color: #eaedf1;
}
.el-menu {
  background-color: #545c64;
}
</style>
