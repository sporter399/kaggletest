var app = new Vue({
    el: '.mount-point',

    data: function() {
        
        return {
            revolvingUtilizationOfUnsecuredLines: []

        };
    },

    computed: {

        debtToCredit: function () {

            c.execute("SELECT RevolvingUtilizationOfUnsecuredLines FROM APPLICANTS;")
            result = c.fetchall()
            this.revolvingUtilizationOfUnsecuredLines.push(result);

                   
            return this.revolvingUtilizationOfUnsecuredLines;
           
        },

    },

    methods: {

    },







});