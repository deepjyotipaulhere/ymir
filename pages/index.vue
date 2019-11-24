<template>
	<div>
		<div class="ui pointing menu">
			<nuxt-link class="active item" to="/">
				Home
			</nuxt-link>
			<nuxt-link class="item" to="/records">
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
		<div class="ui container">
			<button class="ui right floated labeled icon button primary" v-if="uploadedfile!='' && detectedtext==''" @click.prevent="detect" :class="{'loading':loading}">
				<i class="right arrow icon"></i>
				Start Detection
			</button>
			<button class="ui secondary button right floated labeled icon" style="float:right" v-if="detectedtext!=''" @click.prevent="resetall">
				<i class="right arrow icon"></i>
				New Image
			</button>
			<h1>Handwriting Recognition</h1>
			<div class="ui segment">
				<div class="ui two column very relaxed grid">
					<div class="column" style="min-height:300px">
						<no-ssr v-if="uploadedfile==''">
							<file-pond
								name="test"
								ref="test"
								label-idle="Drop files here..."
								allow-multiple="false"
								server="http://localhost:5000/uploadimage"
								accepted-file-types="image/jpeg, image/png"
								v-bind:files="myFiles"
                            	v-on:processfile="addtopreview"
								/>
						</no-ssr>
						<img :src="uploadedfile" alt="" class="ui fluid image" v-else>
					</div>
					<div class="column">
						<p v-html="detectedtext"></p>
					</div>
				</div>
				<div class="ui vertical divider" v-if="uploadedfile!=''">
					
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import vueFilePond from 'vue-filepond';
import 'filepond/dist/filepond.min.css';
import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css';
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type';
import FilePondPluginImagePreview from 'filepond-plugin-image-preview';

const FilePond = vueFilePond( FilePondPluginFileValidateType, FilePondPluginImagePreview );

export default {
	name: 'app',
    data: function() {
        return {
			myFiles: [],
			uploadedfile:'',
			detectedtext:'',
			loading: false
		};
    },
    components: {
        FilePond
    },
    methods: {
		addtopreview(error, file){
			this.uploadedfile=file.serverId
		},
		detect(){
			this.loading=true
			this.$axios.post("http://localhost:5000/detect",{
				filename: this.uploadedfile
			}).then(response=>{
				this.detectedtext=response.data
				this.loading=false
			})
		},
		resetall(){
			this.uploadedfile=''
			this.detectedtext=''
		}
    },
}
</script>

<style>

</style>
