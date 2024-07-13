<template>
  <header_component :jp="true" />

  <router-view />

  <footer_component :jp="true" />
</template>

<style>
/* 共通CSS */
html {
  Overflow-y: scroll
}

body {
  font-family: "Calisto MT";
  background-color: #474646;
}

main {
  color: white;
  padding: 40px;
  padding-left: 280px;
  padding-right: 280px;

  .h-title-design {
    padding: 2%;
    border-left: 5px solid #3e3528;
    background-color: #34343c;
  }
}

@media screen and (max-width: 768px) {
  body {
    font-family: "Baskerville";
  }

  main {
    padding-left: 40px;
    padding-right: 40px;
  }
}
</style>

<script>
import header_component from "./components/header_component.vue";
import footer_component from "./components/footer_component.vue";

export default {
  components: {
    header_component, footer_component,
  }
}
</script>