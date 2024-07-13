<template>
  <VueElementLoading :active="loading" spinner="bar-fade-scale" is-full-screen />

  <header>
    <img src="../img/header.jpg" width="100%">
  </header>

  <header v-if="!jp">
    <nav aria-label="Page navigation" class="pagination_top">
      <ul class="pagination">
        <li class="page-item"><router-link to="./index.html" class="page-link">TOP</router-link></li>
        <li class="page-item"><router-link to="./car.html" class="page-link">Veículos</router-link></li>
        <li class="page-item"><router-link to="./inquiry.html" class="page-link">Inquérito</router-link></li>
        <!-- <li class="page-item"><router-link to="./book.html" class="page-link">Reservas</router-link></li> -->
        <li class="page-item"><a class="page-link" href="./index_jpn.html">Japonês</a></li>
      </ul>
    </nav>
  </header>

  <header v-else>
    <nav aria-label="Page navigation" class="pagination_top">
      <ul class="pagination">
        <li class="page-item"><router-link to="./index_jpn.html" class="page-link">TOP</router-link></li>
        <li class="page-item"><router-link to="./car_jpn.html" class="page-link">車両</router-link></li>
        <li class="page-item"><router-link to="./inquiry_jpn.html" class="page-link">問い合わせ</router-link></li>
        <!-- <li class="page-item"><router-link to="./book_jpn.html" class="page-link">予約表</router-link></li> -->
        <li class="page-item"><a class="page-link" href="./index.html">ポルトガル語</a></li>
      </ul>
    </nav>
  </header>
</template>

<style>
header {

  img {
    height: 250px;
  }

  background-color: #3e3528;

  .pagination_top {
    padding: 1%;
    padding-bottom: 1px;

    .pagination {
      --bs-pagination-border-radius: none;
      --bs-pagination-font-size: 1.2rem;

      .page-link {
        color: white;
        background-color: #3e3528;
        border-style: none;
        border-right: 0.5px solid #686868;
        border-left: 0.5px solid #686868;
        font-size: 0.8rem;
        margin-left: 0;
      }
    }
  }
}

@media screen and (max-width: 768px) {
  header {
    img {
      height: 100px;
    }

    .pagination_top {
      padding: 2%;
      padding-bottom: 1px;
    }
  }
}
</style>

<script>
import common_func_component from "@/components/common_func_component.vue"
import VueElementLoading from "vue-element-loading";

export default {
  mixins: [common_func_component],
  components: {
    VueElementLoading,
  },
  data() {
    return {
      jp: true,
      loading: false,
    }
  },
  async mounted() {
    this.loading = true;
    const timeout = ms => new Promise(resolve => setTimeout(resolve, ms));
    this.jp = await this.common_isjp();
    await timeout(500);
    this.loading = false;
  }
}
</script>
