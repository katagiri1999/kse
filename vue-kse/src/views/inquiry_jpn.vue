<template>
    <VueElementLoading :active="loading" spinner="bar-fade-scale" is-full-screen />

    <body>
        <main>

            <H4 class="h-title-design">問い合わせ</H4>
            <div class="inquiry_body">
                <div class="mb-3">
                    <label for="user_email" class="form-label">Email</label>
                    <input type="email" class="form-control" placeholder="xxx@xxx.xxx" autocomplete="off"
                        v-model="email">
                </div>
                <div class="mb-3">
                    <label for="phone" class="form-label">電話番号</label>
                    <input type="tel" class="form-control" placeholder="xxx-xxxx-xxxx" autocomplete="off"
                        v-model="phone">
                </div>
                <div class="mb-3">
                    <label for="text" class="form-label">問い合わせ</label>
                    <textarea class="form-control" rows="3" placeholder="問い合わせ内容" autocomplete="off"
                        v-model="inquiry"></textarea>
                </div>

                <br>
                <button type="button" class="btn btn-light" @click="send_mail()">送信</button> &emsp; <button
                    type="button" class="btn btn-light" @click="del_content()">リセット</button>
            </div>

            <br><br>

            <H4 class="h-title-design">FAQ</H4>
            <div class="faq">
                <div class="accordion">
                    <div class="accordion-item">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                            data-bs-target="#q1" aria-expanded="false" aria-controls="q1">
                            <div class="question">Q</div>お支払方法は？
                        </button>
                        <div id="q1" class="accordion-collapse collapse">
                            <div class="accordion-body">
                                現金、カード払い対応
                                <br>
                                ※ 領収書をご希望の場合、事前にご連絡ください
                                <br><br>
                                引っ越し/送迎 当日に係員へお支払いください
                            </div>
                        </div>
                    </div>
                </div>

                <br>

                <div class="accordion">
                    <div class="accordion-item">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                            data-bs-target="#q2" aria-expanded="false" aria-controls="q2">
                            <div class="question">Q</div>対応地域は？
                        </button>
                        <div id="q2" class="accordion-collapse collapse">
                            <div class="accordion-body">
                                全国対応
                                <br>
                                ※ 配送車が車道もしくはフェリー等で走行可能な地域
                            </div>
                        </div>
                    </div>
                </div>

                <br>

                <div class="accordion">
                    <div class="accordion-item">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                            data-bs-target="#q3" aria-expanded="false" aria-controls="q3">
                            <div class="question">Q</div>お見積もり方法は？
                        </button>
                        <div id="q3" class="accordion-collapse collapse">
                            <div class="accordion-body">
                                お電話またはお問い合わせフォームからご連絡ください
                                <br><br>
                                TEL (ポルトガル語): <a href="tel:080-3633-1971">080-3633-1971</a>
                                <br>
                                TEL (日本語): <a href="tel:080-4543-6016">080-4543-6016</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </main>
    </body>

</template>

<style scoped>
.inquiry_body {
    padding: 3%;
}

.faq {
    padding: 3%;

    .question {
        font-weight: bold;
        padding-right: 5px;
        color: #155bdc;
    }
}

@media screen and (max-width: 768px) {}
</style>

<script>
import common_func_component from "../components/common_func_component.vue";
import VueElementLoading from "vue-element-loading";

export default {
    mixins: [common_func_component],
    components: {
        VueElementLoading,
    },
    data() {
        return {
            loading: false,
            email: "",
            phone: "",
            inquiry: "",
        }
    },
    methods: {
        async send_mail() {
            var alert_comment1 = "全項目を入力してください";
            var alert_comment2 = "Email形式が不正です";
            var confirm_comment = "送信しますか？";

            if (!this.email || !this.phone || !this.inquiry) {
                alert(alert_comment1)
                return null;
            }

            var pattern = /^[A-Za-z0-9]{1}[A-Za-z0-9_.-]*@{1}[A-Za-z0-9_.-]+.[A-Za-z0-9]+$/;
            if (!pattern.test(this.email)) {
                alert(alert_comment2);
                return null;
            }

            var res = confirm(confirm_comment);
            if (res == true) {

                // send to api
                this.loading = true;
                res = await this.common_requests("email", "POST", { email: this.email, phone: this.phone, inquiry: this.inquiry });
                this.loading = false;

                if (res.status != 200) {
                    alert("Invalid request");
                    throw Error();
                }
                this.del_content();
            }
        },
        async del_content() {
            this.email = "";
            this.phone = "";
            this.inquiry = "";
        }
    }
}
</script>