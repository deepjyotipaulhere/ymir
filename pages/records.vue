<template>
	<div>
		<div class="ui pointing menu">
			<nuxt-link class="item" to="/">
				Home
			</nuxt-link>
			<nuxt-link class="active item" to="/records">
				Display Previous Results
			</nuxt-link>
			<div class="right menu">
				<div class="item">
				<div class="ui transparent icon input">
					<input type="text" placeholder="Search...">
					<i class="search link icon"></i>
				</div>
				</div>
			</div>
		</div>
        <div class="ui container" v-if="loading">
            <div class="ui active dimmer">
                <div class="ui indeterminate text loader">Loading records</div>
            </div>
            <p></p>
        </div>
        <div class="ui container" v-else>
            <h1>Previous Results</h1>
            <div class="ui segment">
                <div class="ui items">
                    <div class="item" v-for="(x,i) in records" :key="i">
                        <div class="image">
                            <img :src="x.file">
                        </div>
                        <div class="content">
                            <div class="description">
                                <p v-html="x.text"></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
	</div>
</template>

<script>
export default {
    data(){
        return {
            loading:true,
            records:[]
        }
    },
    created(){
        this.$axios.get("http://localhost:5000/getrecords").then(response=>{
            this.records=response.data
            this.loading=false
        })
    }
}
</script>