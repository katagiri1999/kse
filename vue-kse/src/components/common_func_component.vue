<script>
export default {
    methods: {
        async common_isjp() {
            if (location.href.includes("_jpn")) {
                return true;
            } else {
                return false;
            }
        },
        async common_requests(func, method, params) {
            var api_url = `${process.env.VUE_APP_API_HOST}/?api_key=${process.env.VUE_APP_API_KEY}&func=${func}`;
            var request_info = { url: api_url, method: method, params: params };
            console.log("request");
            console.log(request_info);

            if (method == "GET" || method == "get") {
                var q_params = new URLSearchParams(params);
                api_url = `${api_url}&${q_params}`;
                var detail = {
                    method: method,
                };
            } else {
                detail = {
                    method: method,
                    body: JSON.stringify(params),
                };
            }

            var res = await fetch(
                api_url,
                detail
            );

            var body = await res.json();

            console.log("response");
            var res_info = { status: res.status, body: body };
            console.log(res_info);

            return res_info;
        }
    }
}
</script>