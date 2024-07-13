<template>

    <body>
        <main>
            <h4 class="h-title-design">予約表</h4>

            <div class="calendar">
                <VueElementLoading background-color="rgba(0,0,0,0.0001)" color="white" :active="loading" />

                <FullCalendar :options="calendarOptions" />
            </div>

            <div class="admin_site">
                <router-link to="./admin_jpn.html">管理者用ページ</router-link>
            </div>
        </main>
    </body>

</template>

<style>
.calendar {
    padding-top: 3%;

    a {
        color: aliceblue;
    }

    thead {
        background-color: #34343c;
    }
}

.admin_site {
    text-align: right;
    padding-top: 8%;
}

@media screen and (max-width: 768px) {}
</style>

<script>
import common_func_component from "../components/common_func_component.vue";
import VueElementLoading from "vue-element-loading";
import FullCalendar from '@fullcalendar/vue3';
import dayGridPlugin from '@fullcalendar/daygrid';

export default {
    mixins: [common_func_component],
    components: { FullCalendar, VueElementLoading },
    data() {
        return {
            calendarOptions: {
                plugins: [dayGridPlugin],
                headerToolbar: {
                    left: "",
                    center: "title",
                    right: "today prev,next"
                },
                initialView: 'dayGridMonth',
                height: "auto",
                titleFormat: { year: 'numeric', month: 'numeric' },
                events: [],
            },
            loading: false,
        }
    },
    async mounted() {
        // get books api
        this.loading = true;
        var res = await this.common_requests("books", "GET", {});

        for (const book of res.body.books) {
            this.calendarOptions.events.push({ title: "✖", date: book, display: "background", color: "red" })
        }
        this.loading = false;
    }
}
</script>