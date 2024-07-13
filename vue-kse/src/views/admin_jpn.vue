<template>
    <VueElementLoading :active="loading" spinner="bar-fade-scale" is-full-screen />

    <body>
        <main>
            <h4 class="h-title-design">管理者用サイト</h4>

            <div v-if="!after_login" class="login_form">
                <div class="mb-3">
                    <label for="input1" class="form-label">ID</label>
                    <input class="form-control" v-model="id">
                </div>
                <div class="mb-3">
                    <label for="input2" class="form-label">PW</label>
                    <input type="password" class="form-control" v-model="password">
                </div>
                <br>
                <button type="button" class="btn btn-light" @click="login()">Login</button>
                <br><br>
            </div>

            <div v-else class="book_editer">
                <div class="calendar">
                    <FullCalendar :options="calendarOptions" />
                </div>
                <button type="button" class="btn btn-light" @click="register()">Save</button>
            </div>
        </main>

    </body>

</template>

<style>
.login_form {
    padding-top: 3%;
    width: 80%;
    padding-left: 15%;
}

.book_editer {

    .btn {
        margin-top: 5%;
    }

    .calendar {
        padding-top: 3%;

        a {
            color: aliceblue;
        }

        thead {
            background-color: #34343c;
        }
    }
}

@media screen and (max-width: 768px) {}
</style>

<script>
import common_func_component from "../components/common_func_component.vue";
import VueElementLoading from "vue-element-loading";
import FullCalendar from '@fullcalendar/vue3';
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction';

export default {
    mixins: [common_func_component],
    components: {
        VueElementLoading, FullCalendar
    },
    data() {
        return {
            loading: false,
            after_login: false,
            id: "",
            password: "",
            calendarOptions: {
                plugins: [dayGridPlugin, interactionPlugin],
                headerToolbar: {
                    left: "",
                    center: "title",
                    right: "today prev,next"
                },
                initialView: 'dayGridMonth',
                height: "auto",
                titleFormat: { year: 'numeric', month: 'numeric' },
                selectable: true,
                events: [],
                dateClick: this.date_click,
            },
        }
    },
    methods: {
        async login() {
            if (!this.id || !this.password) {
                alert("ID, PWを入力してください");
                throw Error();
            }

            // auth api
            this.loading = true;
            var res = await this.common_requests("auth", "POST", { user_id: this.id, password: this.password });
            if (res.status != 200) {
                this.loading = false;
                alert("IDもしくはPWが間違っています。");
                throw Error();
            }
            this.after_login = true;
            sessionStorage.setItem("token", res.body.token);

            // get books api
            res = await this.common_requests("books", "GET", {});

            for (const book of res.body.books) {
                this.calendarOptions.events.push({ title: "✖", date: book, display: "background", color: "red" })
            }

            this.loading = false;
        },
        async date_click(info) {
            var events_str = JSON.stringify(this.calendarOptions.events);

            if (!events_str.includes(info.dateStr)) {
                // add clicked date
                this.calendarOptions.events.push({ title: "✖", date: info.dateStr, display: "background", color: "red" })
            } else {
                // rm clicked date
                var new_events = [];
                for (const book of this.calendarOptions.events) {
                    if (book.date != info.dateStr) {
                        new_events.push(book);
                    }
                }
                this.calendarOptions.events = new_events;
            }
        },
        async register() {
            var arr = [];
            for (const book of this.calendarOptions.events) {
                var today = new Date();
                var target_date = new Date(book.date);

                if (today < target_date) {
                    // 今日以前の予約を削除
                    arr.push(book.date);
                }
            }

            // post books api
            this.loading = true;
            var res = await this.common_requests("books" , "POST", { books: arr, token: sessionStorage.getItem("token") });

            if (res.status != 200) {
                alert("エラーが発生しました。再ログインしてください。");
                window.location.reload();

            } else {
                // get books api
                res = await this.common_requests("books", "GET", {});

                this.calendarOptions.events = [];
                for (const book of res.body.books) {
                    this.calendarOptions.events.push({ title: "✖", date: book, display: "background", color: "red" })
                }
            }
            this.loading = false;
        }
    }
}
</script>