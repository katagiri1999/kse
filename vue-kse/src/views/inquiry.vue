<template>
    <VueElementLoading :active="loading" spinner="bar-fade-scale" is-full-screen />

    <body>
        <main>

            <H4 class="h-title-design">Inquérito</H4>
            <div class="inquiry_body">
                <div class="mb-3">
                    <label for="user_email" class="form-label">Email</label>
                    <input type="email" class="form-control" placeholder="xxx@xxx.xxx" v-model="email">
                </div>
                <div class="mb-3">
                    <label for="phone" class="form-label">Phone</label>
                    <input type="tel" class="form-control" placeholder="xxx-xxxx-xxxx" v-model="phone">
                </div>
                <div class="mb-3">
                    <label for="text" class="form-label">Detalhes</label>
                    <textarea class="form-control" rows="3" placeholder="Detalhes" v-model="inquiry"></textarea>
                </div>

                <br>
                <button type="button" class="btn btn-light" @click="send_mail()">OK</button> &emsp; <button
                    type="button" class="btn btn-light" @click="del_content()">RESET</button>
            </div>

            <br><br>

            <H4 class="h-title-design">FAQ</H4>
            <div class="faq">
                <div class="accordion">
                    <div class="accordion-item">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                            data-bs-target="#q1" aria-expanded="false" aria-controls="q1">
                            <div class="question">Q</div>Como faço para pagar?
                        </button>
                        <div id="q1" class="accordion-collapse collapse">
                            <div class="accordion-body">
                                Pagamento em dinheiro ou cartão de crédito.
                                <br>
                                ※ Se você gostaria de um recibo, entre em contato conosco com antecedência.
                                <br><br>
                                Por favor, pague a equipe no dia da mudança ou transferência.
                            </div>
                        </div>
                    </div>
                </div>

                <br>

                <div class="accordion">
                    <div class="accordion-item">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                            data-bs-target="#q2" aria-expanded="false" aria-controls="q2">
                            <div class="question">Q</div>Quais regiões são suportadas?
                        </button>
                        <div id="q2" class="accordion-collapse collapse">
                            <div class="accordion-body">
                                Suporte nacional no Japão.
                                <br>
                                ※ Áreas onde os veículos de entrega podem viajar em estradas ou balsas, etc.
                            </div>
                        </div>
                    </div>
                </div>

                <br>

                <div class="accordion">
                    <div class="accordion-item">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                            data-bs-target="#q3" aria-expanded="false" aria-controls="q3">
                            <div class="question">Q</div>Como posso obter um orçamento?
                        </button>
                        <div id="q3" class="accordion-collapse collapse">
                            <div class="accordion-body">
                                Entre em contato conosco por telefone ou usando o formulário de consulta.
                                <br><br>
                                TEL (Português): <a href="tel:080-3633-1971">080-3633-1971</a>
                                <br>
                                TEL (Japonês): <a href="tel:080-4543-6016">080-4543-6016</a>
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
            var alert_comment1 = "Preencha todos os campos";
            var alert_comment2 = "Email inválido";
            var confirm_comment = "Quer enviar?";

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