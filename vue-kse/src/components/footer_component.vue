<template>
    <footer v-if="!jp" class="footer">
        <br>
        <h4>KSE・Transport</h4>
        <p>
            〒455-0001 Aichi-ken Nagoya-shi Minato-ku Shitiban-cho 2-11-1 Moru Kyubangai
            <br>
            <a href="mailto:mail@kse-t.jp" target="_blank">mail@kse-t.jp</a>
        </p>
    </footer>

    <footer v-else class="footer">
        <br>
        <h4>KSE・Transport</h4>
        <p>
            〒455-0001 愛知県 名古屋市 港区 七番町 2-11-1 モール九番街
            <br>
            <a href="mailto:mail@kse-t.jp" target="_blank">mail@kse-t.jp</a>
        </p>
    </footer>

    <footer>
        <!-- <a href="https://mybrasilmercado.com/" target="_blank"><img src="./img/logotipo.png" width="30%" class="img-thumbnail"></a>
          <br>
          <a href="https://mybrasilmercado.com/" target="_blank">(Afiliados: MY BRASIL)</a> -->
        <br><br>
        <p>&copy;2021 KSE・Transport All Rights Reserved.</p>
    </footer>
</template>

<style>
footer {
    background-color: #3e3528;
    color: white;
    text-align: center;
    padding: 10px;

    a {
        color: white;
    }
}

@media screen and (max-width: 768px) {
    footer {
        font-size: small;
    }
}
</style>

<script>
import common_func_component from "../components/common_func_component.vue"

export default {
    mixins: [common_func_component],
    data() {
        return {
            jp: true,
        }
    },
    async mounted() {
        this.jp = await this.common_isjp();
    }
}
</script>