<!doctype html>
<html class="">
	<head>
		<meta charset="utf-8" />

		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />

		<meta name="description" content="We’re on a journey to advance and democratize artificial intelligence through open source and open science." />

		<meta property="fb:app_id" content="1321688464574422" />

		<meta name="twitter:card" content="summary_large_image" />

		<meta name="twitter:site" content="@huggingface" />

		<meta name="twitter:image" content="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/huypd1508/wav2vec2-t5-Vietnamese.png" />

		<meta property="og:title" content="modeling_wav2vec2_to_vit5_bottleneck.py · huypd1508/wav2vec2-t5-Vietnamese at main" />

		<meta property="og:type" content="website" />

		<meta property="og:url" content="https://huggingface.co/huypd1508/wav2vec2-t5-Vietnamese/blob/main/modeling_wav2vec2_to_vit5_bottleneck.py" />

		<meta property="og:image" content="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/huypd1508/wav2vec2-t5-Vietnamese.png" />

		<link rel="stylesheet" href="/front/build/kube-4bcc544/style.css" />

		<link rel="preconnect" href="https://fonts.gstatic.com" />

		<link
			href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;1,200;1,300;1,400;1,600;1,700&display=swap"
			rel="stylesheet"
		/>

		<link
			href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&display=swap"
			rel="stylesheet"
		/>

		<link
			rel="preload"
			href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css"
			as="style"
			onload="this.onload=null;this.rel='stylesheet'"
		/>

		<noscript>
			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css" />
		</noscript>
		<script>if (window.matchMedia('(prefers-color-scheme: dark)').matches) { document.documentElement.classList.add('dark'); }</script>
<link rel="canonical" href="https://huggingface.co/huypd1508/wav2vec2-t5-Vietnamese/blob/main/modeling_wav2vec2_to_vit5_bottleneck.py">  <!-- HEAD_svelte-1oal594_START --><style>.blob-line-num::before {
			content: attr(data-line-num);
		}
	</style><!-- HEAD_svelte-1oal594_END -->
		<title>modeling_wav2vec2_to_vit5_bottleneck.py · huypd1508/wav2vec2-t5-Vietnamese at main</title>

		<script defer src="/js/script.js"></script>

		<script>
			(window.plausible =
				window.plausible ||
				function () {
					(plausible.q = plausible.q || []).push(arguments);
				}),
				(plausible.init =
					plausible.init ||
					function (i) {
						plausible.o = i || {};
					});
			plausible.init({
				customProperties: {
					loggedIn: "true",
				},
				endpoint: "/api/event",
			});
		</script>

		<script>
			window.hubConfig = {"features":{"signupDisabled":false},"sshGitUrl":"git@hf.co","moonHttpUrl":"https:\/\/huggingface.co","captchaApiKey":"bd5f2066-93dc-4bdd-a64b-a24646ca3859","datasetViewerPublicUrl":"https:\/\/datasets-server.huggingface.co","stripePublicKey":"pk_live_x2tdjFXBCvXo2FFmMybezpeM00J6gPCAAc","environment":"production","userAgent":"HuggingFace (production)","spacesIframeDomain":"hf.space","spacesApiUrl":"https:\/\/api.hf.space","docSearchKey":"ece5e02e57300e17d152c08056145326e90c4bff3dd07d7d1ae40cf1c8d39cb6","logoDev":{"apiUrl":"https:\/\/img.logo.dev\/","apiKey":"pk_UHS2HZOeRnaSOdDp7jbd5w"}};
		</script>
		<script type="text/javascript" src="https://de5282c3ca0c.edge.sdk.awswaf.com/de5282c3ca0c/526cf06acb0d/challenge.js" defer></script> 
	</head>
	<body class="flex flex-col min-h-dvh bg-white dark:bg-gray-950 text-black ViewerBlobPage">
		<div class="flex min-h-dvh flex-col"><div class="SVELTE_HYDRATER contents" data-target="DeviceProvider" data-props="{}"></div>
	<div class="SVELTE_HYDRATER contents" data-target="SystemThemeMonitor" data-props="{&quot;isLoggedIn&quot;:true,&quot;theme&quot;:&quot;system&quot;}"></div>

	<div class="SVELTE_HYDRATER contents" data-target="MainHeader" data-props="{&quot;authLight&quot;:{&quot;csrfToken&quot;:&quot;eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3NjU4MTAxMDA5OTIsInVzZXJJZCI6IjY2ZjYwYTVlODExYmI0ZTkzN2Y0ZTM0NSJ9LCJzaWduYXR1cmUiOiIwODU2MWE4NjFjZDFhNDNiZjI4MjE5ZGY5MGI3MWEzZWVlM2FlZjhkYmNiMzFlMDQzM2RiMjdlNWE2YTI4NmNhIn0=&quot;,&quot;hasHfLevelAccess&quot;:false,&quot;u&quot;:{&quot;avatarUrl&quot;:&quot;/avatars/16a7825f33635ba39f10147b19754fb6.svg&quot;,&quot;isPro&quot;:false,&quot;orgs&quot;:[],&quot;user&quot;:&quot;huypd1508&quot;,&quot;canPost&quot;:false,&quot;canHaveBilling&quot;:true,&quot;canCreateOrg&quot;:true,&quot;theme&quot;:&quot;system&quot;,&quot;notifications&quot;:{&quot;org_suggestions&quot;:false},&quot;hardwareItems&quot;:[],&quot;hardwareItemsPrivate&quot;:false,&quot;usage&quot;:{&quot;storage&quot;:{&quot;summary&quot;:{&quot;space&quot;:{&quot;used&quot;:0,&quot;usedPrivate&quot;:0,&quot;usedPublic&quot;:0,&quot;count&quot;:1},&quot;model&quot;:{&quot;used&quot;:36856368131,&quot;usedPrivate&quot;:0,&quot;usedPublic&quot;:36856368131,&quot;count&quot;:11}},&quot;used&quot;:36856368131,&quot;count&quot;:12,&quot;usedPrivate&quot;:0,&quot;usedPublic&quot;:36856368131},&quot;inference&quot;:{&quot;usedNanoUsd&quot;:0,&quot;numRequests&quot;:0,&quot;providerDetails&quot;:[],&quot;periodEnd&quot;:&quot;2025-12-31T23:59:59.999Z&quot;,&quot;periodStart&quot;:&quot;2025-12-01T00:00:00.000Z&quot;,&quot;includedNanoUsd&quot;:100000000,&quot;limitNanoUsd&quot;:100000000,&quot;lastUpdated&quot;:&quot;2025-12-14T14:48:17.984Z&quot;},&quot;zeroGpu&quot;:{&quot;base&quot;:210,&quot;current&quot;:210,&quot;lastUpdated&quot;:&quot;2025-12-14T14:48:17.984Z&quot;}},&quot;welcomeLinks&quot;:[],&quot;hasProOrOrgPaidPlan&quot;:false}},&quot;classNames&quot;:&quot;&quot;,&quot;avatarUrl&quot;:&quot;/avatars/16a7825f33635ba39f10147b19754fb6.svg&quot;,&quot;isWide&quot;:false,&quot;isZh&quot;:false,&quot;user&quot;:&quot;huypd1508&quot;,&quot;unreadNotifications&quot;:0,&quot;unreadChangelogCount&quot;:3,&quot;csrf&quot;:&quot;eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3NjU4MTAxMDA5OTIsInVzZXJJZCI6IjY2ZjYwYTVlODExYmI0ZTkzN2Y0ZTM0NSJ9LCJzaWduYXR1cmUiOiIwODU2MWE4NjFjZDFhNDNiZjI4MjE5ZGY5MGI3MWEzZWVlM2FlZjhkYmNiMzFlMDQzM2RiMjdlNWE2YTI4NmNhIn0=&quot;,&quot;canCreateOrg&quot;:true,&quot;isPro&quot;:false}"><header class="border-b border-gray-100 "><div class="w-full px-4 container flex h-16 items-center"><div class="flex flex-1 items-center"><a class="mr-5 flex flex-none items-center lg:mr-6" href="/"><img alt="Hugging Face's logo" class="w-7 md:mr-2" src="/front/assets/huggingface_logo-noborder.svg">
				<span class="hidden whitespace-nowrap text-lg font-bold md:block">Hugging Face</span></a>
			<div class="relative flex-1 lg:max-w-sm mr-2 sm:mr-4 md:mr-3 xl:mr-6"><input autocomplete="off" class="w-full dark:bg-gray-950 pl-8 form-input-alt h-9 pr-3 focus:shadow-xl " name="" placeholder="Search models, datasets, users..."   spellcheck="false" type="text" value="">
	<svg class="absolute left-2.5 text-gray-400 top-1/2 transform -translate-y-1/2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M30 28.59L22.45 21A11 11 0 1 0 21 22.45L28.59 30zM5 14a9 9 0 1 1 9 9a9 9 0 0 1-9-9z" fill="currentColor"></path></svg>
	</div>
			<div class="flex flex-none items-center justify-center p-0.5 place-self-stretch lg:hidden"><button class="relative z-40 flex h-6 w-8 items-center justify-center" type="button"><svg width="1em" height="1em" viewBox="0 0 10 10" class="text-xl" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.65039 2.9999C1.65039 2.8066 1.80709 2.6499 2.00039 2.6499H8.00039C8.19369 2.6499 8.35039 2.8066 8.35039 2.9999C8.35039 3.1932 8.19369 3.3499 8.00039 3.3499H2.00039C1.80709 3.3499 1.65039 3.1932 1.65039 2.9999ZM1.65039 4.9999C1.65039 4.8066 1.80709 4.6499 2.00039 4.6499H8.00039C8.19369 4.6499 8.35039 4.8066 8.35039 4.9999C8.35039 5.1932 8.19369 5.3499 8.00039 5.3499H2.00039C1.80709 5.3499 1.65039 5.1932 1.65039 4.9999ZM2.00039 6.6499C1.80709 6.6499 1.65039 6.8066 1.65039 6.9999C1.65039 7.1932 1.80709 7.3499 2.00039 7.3499H8.00039C8.19369 7.3499 8.35039 7.1932 8.35039 6.9999C8.35039 6.8066 8.19369 6.6499 8.00039 6.6499H2.00039Z"></path></svg>
		</button>

	</div></div>
		<nav aria-label="Main" class="ml-auto hidden lg:block"><ul class="flex items-center gap-x-1 2xl:gap-x-2"><li class="hover:text-indigo-700"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/models"><svg class="mr-1.5 text-gray-400 group-hover:text-indigo-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
						Models</a>
				</li><li class="hover:text-red-700"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/datasets"><svg class="mr-1.5 text-gray-400 group-hover:text-red-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
						Datasets</a>
				</li><li class="hover:text-blue-700"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/spaces"><svg class="mr-1.5 text-gray-400 group-hover:text-blue-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 25 25"><path opacity=".5" d="M6.016 14.674v4.31h4.31v-4.31h-4.31ZM14.674 14.674v4.31h4.31v-4.31h-4.31ZM6.016 6.016v4.31h4.31v-4.31h-4.31Z" fill="currentColor"></path><path opacity=".75" fill-rule="evenodd" clip-rule="evenodd" d="M3 4.914C3 3.857 3.857 3 4.914 3h6.514c.884 0 1.628.6 1.848 1.414a5.171 5.171 0 0 1 7.31 7.31c.815.22 1.414.964 1.414 1.848v6.514A1.914 1.914 0 0 1 20.086 22H4.914A1.914 1.914 0 0 1 3 20.086V4.914Zm3.016 1.102v4.31h4.31v-4.31h-4.31Zm0 12.968v-4.31h4.31v4.31h-4.31Zm8.658 0v-4.31h4.31v4.31h-4.31Zm0-10.813a2.155 2.155 0 1 1 4.31 0 2.155 2.155 0 0 1-4.31 0Z" fill="currentColor"></path><path opacity=".25" d="M16.829 6.016a2.155 2.155 0 1 0 0 4.31 2.155 2.155 0 0 0 0-4.31Z" fill="currentColor"></path></svg>
						Spaces</a>
				</li><li class="max-xl:hidden relative"><div class="relative ">
	<button class="group flex items-center px-2 py-0.5 dark:text-gray-300 hover:text-yellow-700 dark:hover:text-gray-100 " type="button">
		<svg class="mr-1.5 mr-1.5 text-gray-400 text-yellow-500! group-hover:text-yellow-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M20.6081 3C21.7684 3 22.8053 3.49196 23.5284 4.38415C23.9756 4.93678 24.4428 5.82749 24.4808 7.16133C24.9674 7.01707 25.4353 6.93643 25.8725 6.93643C26.9833 6.93643 27.9865 7.37587 28.696 8.17411C29.6075 9.19872 30.0124 10.4579 29.8361 11.7177C29.7523 12.3177 29.5581 12.8555 29.2678 13.3534C29.8798 13.8646 30.3306 14.5763 30.5485 15.4322C30.719 16.1032 30.8939 17.5006 29.9808 18.9403C30.0389 19.0342 30.0934 19.1319 30.1442 19.2318C30.6932 20.3074 30.7283 21.5229 30.2439 22.6548C29.5093 24.3704 27.6841 25.7219 24.1397 27.1727C21.9347 28.0753 19.9174 28.6523 19.8994 28.6575C16.9842 29.4379 14.3477 29.8345 12.0653 29.8345C7.87017 29.8345 4.8668 28.508 3.13831 25.8921C0.356375 21.6797 0.754104 17.8269 4.35369 14.1131C6.34591 12.058 7.67023 9.02782 7.94613 8.36275C8.50224 6.39343 9.97271 4.20438 12.4172 4.20438H12.4179C12.6236 4.20438 12.8314 4.2214 13.0364 4.25468C14.107 4.42854 15.0428 5.06476 15.7115 6.02205C16.4331 5.09583 17.134 4.359 17.7682 3.94323C18.7242 3.31737 19.6794 3 20.6081 3ZM20.6081 5.95917C20.2427 5.95917 19.7963 6.1197 19.3039 6.44225C17.7754 7.44319 14.8258 12.6772 13.7458 14.7131C13.3839 15.3952 12.7655 15.6837 12.2086 15.6837C11.1036 15.6837 10.2408 14.5497 12.1076 13.1085C14.9146 10.9402 13.9299 7.39584 12.5898 7.1776C12.5311 7.16799 12.4731 7.16355 12.4172 7.16355C11.1989 7.16355 10.6615 9.33114 10.6615 9.33114C10.6615 9.33114 9.0863 13.4148 6.38031 16.206C3.67434 18.998 3.5346 21.2388 5.50675 24.2246C6.85185 26.2606 9.42666 26.8753 12.0653 26.8753C14.8021 26.8753 17.6077 26.2139 19.1799 25.793C19.2574 25.7723 28.8193 22.984 27.6081 20.6107C27.4046 20.212 27.0693 20.0522 26.6471 20.0522C24.9416 20.0522 21.8393 22.6726 20.5057 22.6726C20.2076 22.6726 19.9976 22.5416 19.9116 22.222C19.3433 20.1173 28.552 19.2325 27.7758 16.1839C27.639 15.6445 27.2677 15.4256 26.746 15.4263C24.4923 15.4263 19.4358 19.5181 18.3759 19.5181C18.2949 19.5181 18.2368 19.4937 18.2053 19.4419C17.6743 18.557 17.9653 17.9394 21.7082 15.6009C25.4511 13.2617 28.0783 11.8545 26.5841 10.1752C26.4121 9.98141 26.1684 9.8956 25.8725 9.8956C23.6001 9.89634 18.2311 14.9403 18.2311 14.9403C18.2311 14.9403 16.7821 16.496 15.9057 16.496C15.7043 16.496 15.533 16.4139 15.4169 16.2112C14.7956 15.1296 21.1879 10.1286 21.5484 8.06535C21.7928 6.66715 21.3771 5.95917 20.6081 5.95917Z" fill="#FF9D00"></path><path d="M5.50686 24.2246C3.53472 21.2387 3.67446 18.9979 6.38043 16.206C9.08641 13.4147 10.6615 9.33111 10.6615 9.33111C10.6615 9.33111 11.2499 6.95933 12.59 7.17757C13.93 7.39581 14.9139 10.9401 12.1069 13.1084C9.29997 15.276 12.6659 16.7489 13.7459 14.713C14.8258 12.6772 17.7747 7.44316 19.304 6.44221C20.8326 5.44128 21.9089 6.00204 21.5484 8.06532C21.188 10.1286 14.795 15.1295 15.4171 16.2118C16.0391 17.2934 18.2312 14.9402 18.2312 14.9402C18.2312 14.9402 25.0907 8.49588 26.5842 10.1752C28.0776 11.8545 25.4512 13.2616 21.7082 15.6008C17.9646 17.9393 17.6744 18.557 18.2054 19.4418C18.7372 20.3266 26.9998 13.1351 27.7759 16.1838C28.5513 19.2324 19.3434 20.1173 19.9117 22.2219C20.48 24.3274 26.3979 18.2382 27.6082 20.6107C28.8193 22.9839 19.2574 25.7722 19.18 25.7929C16.0914 26.62 8.24723 28.3726 5.50686 24.2246Z" fill="#FFD21E"></path></svg>
			Community
		</button>
	
	
	</div>
				</li><li class="hover:text-yellow-700"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/docs"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="mr-1.5 text-gray-400 group-hover:text-yellow-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><path d="m2.28 3.7-.3.16a.67.67 0 0 0-.34.58v8.73l.01.04.02.07.01.04.03.06.02.04.02.03.04.06.05.05.04.04.06.04.06.04.08.04.08.02h.05l.07.02h.11l.04-.01.07-.02.03-.01.07-.03.22-.12a5.33 5.33 0 0 1 5.15.1.67.67 0 0 0 .66 0 5.33 5.33 0 0 1 5.33 0 .67.67 0 0 0 1-.58V4.36a.67.67 0 0 0-.34-.5l-.3-.17v7.78a.63.63 0 0 1-.87.59 4.9 4.9 0 0 0-4.35.35l-.65.39a.29.29 0 0 1-.15.04.29.29 0 0 1-.16-.04l-.65-.4a4.9 4.9 0 0 0-4.34-.34.63.63 0 0 1-.87-.59V3.7Z" fill="currentColor" class="dark:opacity-40"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M8 3.1a5.99 5.99 0 0 0-5.3-.43.66.66 0 0 0-.42.62v8.18c0 .45.46.76.87.59a4.9 4.9 0 0 1 4.34.35l.65.39c.05.03.1.04.16.04.05 0 .1-.01.15-.04l.65-.4a4.9 4.9 0 0 1 4.35-.34.63.63 0 0 0 .86-.59V3.3a.67.67 0 0 0-.41-.62 5.99 5.99 0 0 0-5.3.43l-.3.17L8 3.1Zm.73 1.87a.43.43 0 1 0-.86 0v5.48a.43.43 0 0 0 .86 0V4.97Z" fill="currentColor" class="opacity-40 dark:opacity-100"></path><path d="M8.73 4.97a.43.43 0 1 0-.86 0v5.48a.43.43 0 1 0 .86 0V4.96Z" fill="currentColor" class="dark:opacity-40"></path></svg>
						Docs</a>
				</li><li class="hover:text-black dark:hover:text-white max-2xl:hidden"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/enterprise"><svg class="mr-1.5 text-gray-400 group-hover:text-black dark:group-hover:text-white" xmlns="http://www.w3.org/2000/svg" fill="none" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 12 12"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.9 1.35a3.16 3.16 0 0 0-2.8 2.07L.37 8.58C0 9.71.7 10.65 1.86 10.65H7.3a3.2 3.2 0 0 0 2.84-2.07l1.67-5.16c.36-1.13-.3-2.07-1.46-2.07H4.91Zm.4 2.07L3.57 8.47h3.57l.36-1.12H5.4l.28-.91h1.75l.4-1.1H6.07l.3-.83h2l.36-1.1H5.27h.04Z" fill="currentColor"></path></svg>
						Enterprise</a>
				</li>

		<li><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/pricing">Pricing
			</a></li>

		<li><div class="relative group">
	<button class="px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-600 flex items-center " type="button">
		<svg class=" text-gray-500 w-5 group-hover:text-gray-400 dark:text-gray-300 dark:group-hover:text-gray-100" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 32 18" preserveAspectRatio="xMidYMid meet"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 3.30221C14.4504 2.836 14.8284 2.45807 15.2946 2.45807H28.4933C28.9595 2.45807 29.3374 2.836 29.3374 3.30221C29.3374 3.76842 28.9595 4.14635 28.4933 4.14635H15.2946C14.8284 4.14635 14.4504 3.76842 14.4504 3.30221Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 9.00002C14.4504 8.53382 14.8284 8.15588 15.2946 8.15588H28.4933C28.9595 8.15588 29.3374 8.53382 29.3374 9.00002C29.3374 9.46623 28.9595 9.84417 28.4933 9.84417H15.2946C14.8284 9.84417 14.4504 9.46623 14.4504 9.00002Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 14.6978C14.4504 14.2316 14.8284 13.8537 15.2946 13.8537H28.4933C28.9595 13.8537 29.3374 14.2316 29.3374 14.6978C29.3374 15.164 28.9595 15.542 28.4933 15.542H15.2946C14.8284 15.542 14.4504 15.164 14.4504 14.6978Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M1.94549 6.87377C2.27514 6.54411 2.80962 6.54411 3.13928 6.87377L6.23458 9.96907L9.32988 6.87377C9.65954 6.54411 10.194 6.54411 10.5237 6.87377C10.8533 7.20343 10.8533 7.73791 10.5237 8.06756L6.23458 12.3567L1.94549 8.06756C1.61583 7.73791 1.61583 7.20343 1.94549 6.87377Z" fill="currentColor"></path></svg>
			
		</button>
	
	
	</div></li>
		<li><hr class="h-5 w-0.5 border-none bg-gray-100 dark:bg-gray-800"></li>
		<li><form action="/logout" method="POST" class="hidden"><input type="hidden" name="csrf" value="eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3NjU4MTAxMDA5OTIsInVzZXJJZCI6IjY2ZjYwYTVlODExYmI0ZTkzN2Y0ZTM0NSJ9LCJzaWduYXR1cmUiOiIwODU2MWE4NjFjZDFhNDNiZjI4MjE5ZGY5MGI3MWEzZWVlM2FlZjhkYmNiMzFlMDQzM2RiMjdlNWE2YTI4NmNhIn0="></form>
<div class="relative ml-2 w-[1.38rem] h-[1.38rem] ">
	<button class="ml-auto rounded-full ring-2 group ring-indigo-400 focus:ring-blue-500 hover:ring-offset-1 focus:ring-offset-1 focus:outline-hidden outline-hidden dark:ring-offset-gray-950 " type="button">
		
		<div class="relative"><img alt="" class="h-[1.38rem] w-[1.38rem] select-none overflow-hidden rounded-full" src="/avatars/16a7825f33635ba39f10147b19754fb6.svg" crossorigin="anonymous">
			</div>
	
		</button>
	
	
	</div></li></ul></nav></div></header></div>
	
	
	
	<div class="SVELTE_HYDRATER contents" data-target="SSOBanner" data-props="{&quot;organizations&quot;:[]}"></div>
	

	<main class="flex flex-1 flex-col">
	<div class="SVELTE_HYDRATER contents" data-target="ModelHeader" data-props="{&quot;activeTab&quot;:&quot;files&quot;,&quot;authLight&quot;:{&quot;csrfToken&quot;:&quot;eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3NjU4MTAxMDA5OTIsInVzZXJJZCI6IjY2ZjYwYTVlODExYmI0ZTkzN2Y0ZTM0NSJ9LCJzaWduYXR1cmUiOiIwODU2MWE4NjFjZDFhNDNiZjI4MjE5ZGY5MGI3MWEzZWVlM2FlZjhkYmNiMzFlMDQzM2RiMjdlNWE2YTI4NmNhIn0=&quot;,&quot;hasHfLevelAccess&quot;:false,&quot;u&quot;:{&quot;avatarUrl&quot;:&quot;/avatars/16a7825f33635ba39f10147b19754fb6.svg&quot;,&quot;isPro&quot;:false,&quot;orgs&quot;:[],&quot;user&quot;:&quot;huypd1508&quot;,&quot;canPost&quot;:false,&quot;canHaveBilling&quot;:true,&quot;canCreateOrg&quot;:true,&quot;theme&quot;:&quot;system&quot;,&quot;notifications&quot;:{&quot;org_suggestions&quot;:false},&quot;hardwareItems&quot;:[],&quot;hardwareItemsPrivate&quot;:false,&quot;usage&quot;:{&quot;storage&quot;:{&quot;summary&quot;:{&quot;space&quot;:{&quot;used&quot;:0,&quot;usedPrivate&quot;:0,&quot;usedPublic&quot;:0,&quot;count&quot;:1},&quot;model&quot;:{&quot;used&quot;:36856368131,&quot;usedPrivate&quot;:0,&quot;usedPublic&quot;:36856368131,&quot;count&quot;:11}},&quot;used&quot;:36856368131,&quot;count&quot;:12,&quot;usedPrivate&quot;:0,&quot;usedPublic&quot;:36856368131},&quot;inference&quot;:{&quot;usedNanoUsd&quot;:0,&quot;numRequests&quot;:0,&quot;providerDetails&quot;:[],&quot;periodEnd&quot;:&quot;2025-12-31T23:59:59.999Z&quot;,&quot;periodStart&quot;:&quot;2025-12-01T00:00:00.000Z&quot;,&quot;includedNanoUsd&quot;:100000000,&quot;limitNanoUsd&quot;:100000000,&quot;lastUpdated&quot;:&quot;2025-12-14T14:48:17.984Z&quot;},&quot;zeroGpu&quot;:{&quot;base&quot;:210,&quot;current&quot;:210,&quot;lastUpdated&quot;:&quot;2025-12-14T14:48:17.984Z&quot;}},&quot;welcomeLinks&quot;:[],&quot;hasProOrOrgPaidPlan&quot;:false}},&quot;author&quot;:{&quot;_id&quot;:&quot;66f60a5e811bb4e937f4e345&quot;,&quot;avatarUrl&quot;:&quot;/avatars/16a7825f33635ba39f10147b19754fb6.svg&quot;,&quot;fullname&quot;:&quot;Phan Đức Huy&quot;,&quot;name&quot;:&quot;huypd1508&quot;,&quot;type&quot;:&quot;user&quot;,&quot;isPro&quot;:false,&quot;isHf&quot;:false,&quot;isHfAdmin&quot;:false,&quot;isMod&quot;:false,&quot;isUserFollowing&quot;:false},&quot;canReadRepoSettings&quot;:true,&quot;canWriteRepoContent&quot;:true,&quot;canDisable&quot;:false,&quot;model&quot;:{&quot;author&quot;:&quot;huypd1508&quot;,&quot;cardData&quot;:{&quot;library_name&quot;:&quot;transformers&quot;,&quot;tags&quot;:[]},&quot;cardExists&quot;:true,&quot;config&quot;:{&quot;architectures&quot;:[&quot;Wav2Vec2ToVit5WithAdapter&quot;],&quot;model_type&quot;:&quot;wav2vec2_to_vit5_bottleneck&quot;,&quot;auto_map&quot;:{&quot;AutoConfig&quot;:&quot;configuration_wav2vec2_to_vit5_bottleneck.Wav2Vec2ToVit5BottleneckConfig&quot;,&quot;AutoModelForSpeechSeq2Seq&quot;:&quot;modeling_wav2vec2_to_vit5_bottleneck.Wav2Vec2ToVit5WithAdapter&quot;}},&quot;createdAt&quot;:&quot;2025-10-04T13:41:07.000Z&quot;,&quot;discussionsDisabled&quot;:false,&quot;discussionsSorting&quot;:&quot;recently-created&quot;,&quot;downloads&quot;:356,&quot;downloadsAllTime&quot;:522,&quot;id&quot;:&quot;huypd1508/wav2vec2-t5-Vietnamese&quot;,&quot;isLikedByUser&quot;:false,&quot;watched&quot;:{&quot;isWatching&quot;:true,&quot;isMuted&quot;:false,&quot;mode&quot;:&quot;global&quot;},&quot;availableInferenceProviders&quot;:[],&quot;inference&quot;:&quot;&quot;,&quot;lastModified&quot;:&quot;2025-12-14T02:41:54.000Z&quot;,&quot;likes&quot;:0,&quot;pipeline_tag&quot;:&quot;automatic-speech-recognition&quot;,&quot;library_name&quot;:&quot;transformers&quot;,&quot;librariesOther&quot;:[],&quot;trackDownloads&quot;:true,&quot;model-index&quot;:null,&quot;private&quot;:false,&quot;repoType&quot;:&quot;model&quot;,&quot;gated&quot;:false,&quot;tags&quot;:[&quot;transformers&quot;,&quot;safetensors&quot;,&quot;wav2vec2_to_vit5_bottleneck&quot;,&quot;automatic-speech-recognition&quot;,&quot;custom_code&quot;,&quot;arxiv:1910.09700&quot;,&quot;region:us&quot;],&quot;tag_objs&quot;:[{&quot;id&quot;:&quot;automatic-speech-recognition&quot;,&quot;label&quot;:&quot;Automatic Speech Recognition&quot;,&quot;type&quot;:&quot;pipeline_tag&quot;,&quot;subType&quot;:&quot;audio&quot;},{&quot;id&quot;:&quot;transformers&quot;,&quot;label&quot;:&quot;Transformers&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;safetensors&quot;,&quot;label&quot;:&quot;Safetensors&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;wav2vec2_to_vit5_bottleneck&quot;,&quot;label&quot;:&quot;wav2vec2_to_vit5_bottleneck&quot;,&quot;type&quot;:&quot;other&quot;,&quot;clickable&quot;:true},{&quot;id&quot;:&quot;custom_code&quot;,&quot;label&quot;:&quot;custom_code&quot;,&quot;type&quot;:&quot;other&quot;,&quot;clickable&quot;:true},{&quot;id&quot;:&quot;arxiv:1910.09700&quot;,&quot;label&quot;:&quot;arxiv:1910.09700&quot;,&quot;type&quot;:&quot;arxiv&quot;,&quot;extra&quot;:{&quot;paperTitle&quot;:&quot;Quantifying the Carbon Emissions of Machine Learning&quot;}},{&quot;type&quot;:&quot;region&quot;,&quot;label&quot;:&quot;🇺🇸 Region: US&quot;,&quot;id&quot;:&quot;region:us&quot;}],&quot;transformersInfo&quot;:{&quot;auto_model&quot;:&quot;AutoModelForSpeechSeq2Seq&quot;,&quot;custom_class&quot;:&quot;modeling_wav2vec2_to_vit5_bottleneck.Wav2Vec2ToVit5WithAdapter&quot;,&quot;pipeline_tag&quot;:&quot;automatic-speech-recognition&quot;},&quot;safetensors&quot;:{&quot;parameters&quot;:{&quot;F32&quot;:322296448},&quot;total&quot;:322296448,&quot;sharded&quot;:false},&quot;hasBlockedOids&quot;:false,&quot;region&quot;:&quot;us&quot;,&quot;isQuantized&quot;:false},&quot;discussionsStats&quot;:{&quot;closed&quot;:0,&quot;open&quot;:0,&quot;total&quot;:0},&quot;u&quot;:{&quot;avatarUrl&quot;:&quot;/avatars/16a7825f33635ba39f10147b19754fb6.svg&quot;,&quot;isPro&quot;:false,&quot;fullname&quot;:&quot;Phan Đức Huy&quot;,&quot;user&quot;:&quot;huypd1508&quot;,&quot;orgs&quot;:[],&quot;signup&quot;:{},&quot;isHf&quot;:false,&quot;isMod&quot;:false,&quot;type&quot;:&quot;user&quot;,&quot;theme&quot;:&quot;system&quot;,&quot;canPay&quot;:false,&quot;spacesAvailableFlavors&quot;:[&quot;cpu-basic&quot;,&quot;cpu-upgrade&quot;,&quot;zero-a10g&quot;,&quot;t4-small&quot;,&quot;t4-medium&quot;,&quot;l4x1&quot;,&quot;l4x4&quot;,&quot;l40sx1&quot;,&quot;l40sx4&quot;,&quot;l40sx8&quot;,&quot;a10g-small&quot;,&quot;a10g-large&quot;,&quot;a10g-largex2&quot;,&quot;a10g-largex4&quot;,&quot;a100-large&quot;,&quot;h100&quot;,&quot;h100x8&quot;],&quot;canPost&quot;:false,&quot;billingMode&quot;:&quot;postpaid&quot;,&quot;currentBalanceUsd&quot;:0},&quot;query&quot;:{},&quot;inferenceContextData&quot;:{&quot;billableEntities&quot;:[{&quot;type&quot;:&quot;user&quot;,&quot;name&quot;:&quot;huypd1508&quot;,&quot;avatarUrl&quot;:&quot;/avatars/16a7825f33635ba39f10147b19754fb6.svg&quot;,&quot;isPro&quot;:false}],&quot;entityName2Providers&quot;:{}}}"><header class="bg-linear-to-t border-b border-gray-100 pt-6 sm:pt-9 from-purple-500/8 dark:from-purple-500/20 to-white to-70%  dark:to-gray-950"><div class="container relative "><h1 class="flex flex-wrap items-center max-md:leading-tight mb-3 text-lg max-sm:gap-y-1.5 md:text-xl">
			<div class="group flex flex-none items-center"><div class="relative mr-1 flex items-center">

			

<span class="inline-block "><span class="contents"><a href="/huypd1508" class="text-gray-400 hover:text-blue-600"><img alt="" class="size-3.5 rounded-full  flex-none select-none" src="/avatars/16a7825f33635ba39f10147b19754fb6.svg" crossorigin="anonymous"></a></span>
	</span></div>
		

<span class="inline-block "><span class="contents"><a href="/huypd1508" class="text-gray-400 hover:text-blue-600">huypd1508</a></span>
	</span>
		<div class="mx-0.5 text-gray-300">/</div></div>

<div class="max-w-full "><a class="break-words font-mono font-semibold hover:text-blue-600 " href="/huypd1508/wav2vec2-t5-Vietnamese">wav2vec2-t5-Vietnamese</a>
	<button class="text-sm mr-4 focus:outline-hidden inline-flex cursor-pointer items-center text-sm  mx-0.5   text-gray-600 " title="Copy model name to clipboard" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
		</button></div>
			<div class="inline-flex items-center overflow-hidden whitespace-nowrap rounded-md border bg-white text-sm leading-none text-gray-500  mr-2"><button class="relative flex items-center overflow-hidden from-red-50 to-transparent dark:from-red-900 px-1.5 py-1 hover:bg-linear-to-t focus:outline-hidden"  title="Like"><svg class="left-1.5 absolute" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.45,6a5.47,5.47,0,0,1,3.91,1.64,5.7,5.7,0,0,1,0,8L16,26.13,5.64,15.64a5.7,5.7,0,0,1,0-8,5.48,5.48,0,0,1,7.82,0L16,10.24l2.53-2.58A5.44,5.44,0,0,1,22.45,6m0-2a7.47,7.47,0,0,0-5.34,2.24L16,7.36,14.89,6.24a7.49,7.49,0,0,0-10.68,0,7.72,7.72,0,0,0,0,10.82L16,29,27.79,17.06a7.72,7.72,0,0,0,0-10.82A7.49,7.49,0,0,0,22.45,4Z"></path></svg>

		
		<span class="ml-4 pl-0.5 ">like</span></button>
	<button class="focus:outline-hidden flex items-center border-l px-1.5 py-1 text-gray-400 hover:bg-gray-50 focus:bg-gray-100 dark:hover:bg-gray-900 dark:focus:bg-gray-800" title="See users who liked this repository">0</button></div>


			
			
	</h1>
		<div class="mb-3 flex flex-wrap md:mb-4">
	<a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?pipeline_tag=automatic-speech-recognition"><div class="tag   tag-white "><div class="tag-ico -ml-2 tag-ico-green"><svg class="-mr-0.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 18 18"><path fill-rule="evenodd" clip-rule="evenodd" d="M8.38893 3.42133C7.9778 3.14662 7.49446 3 7 3C6.33696 3 5.70108 3.26339 5.23223 3.73223C4.76339 4.20107 4.5 4.83696 4.5 5.5C4.5 5.99445 4.64662 6.4778 4.92133 6.88893C5.19603 7.30005 5.58648 7.62048 6.04329 7.8097C6.50011 7.99892 7.00278 8.04843 7.48773 7.95196C7.97268 7.8555 8.41814 7.6174 8.76777 7.26777C9.1174 6.91814 9.3555 6.47268 9.45197 5.98773C9.54843 5.50277 9.49892 5.00011 9.3097 4.54329C9.12048 4.08648 8.80005 3.69603 8.38893 3.42133ZM5.05551 2.58986C5.63108 2.20527 6.30777 2 7 2C7.92826 2 8.8185 2.36875 9.47488 3.02513C10.1313 3.6815 10.5 4.57174 10.5 5.5C10.5 6.19223 10.2947 6.86892 9.91015 7.4445C9.52556 8.02007 8.97894 8.46867 8.33939 8.73358C7.69985 8.99849 6.99612 9.0678 6.31719 8.93275C5.63825 8.7977 5.01461 8.46436 4.52513 7.97487C4.03564 7.48539 3.7023 6.86175 3.56725 6.18282C3.4322 5.50388 3.50152 4.80015 3.76642 4.16061C4.03133 3.52107 4.47993 2.97444 5.05551 2.58986ZM14.85 9.6425L15.7075 10.5C15.8005 10.5927 15.8743 10.7029 15.9245 10.8242C15.9747 10.9456 16.0004 11.0757 16 11.207V16H2V13.5C2.00106 12.5721 2.37015 11.6824 3.0263 11.0263C3.68244 10.3701 4.57207 10.0011 5.5 10H8.5C9.42793 10.0011 10.3176 10.3701 10.9737 11.0263C11.6299 11.6824 11.9989 12.5721 12 13.5V15H15V11.207L14.143 10.35C13.9426 10.4476 13.7229 10.4989 13.5 10.5C13.2033 10.5 12.9133 10.412 12.6666 10.2472C12.42 10.0824 12.2277 9.84811 12.1142 9.57403C12.0006 9.29994 11.9709 8.99834 12.0288 8.70737C12.0867 8.41639 12.2296 8.14912 12.4393 7.93934C12.6491 7.72956 12.9164 7.5867 13.2074 7.52882C13.4983 7.47094 13.7999 7.50065 14.074 7.61418C14.3481 7.72771 14.5824 7.91997 14.7472 8.16665C14.912 8.41332 15 8.70333 15 9C14.9988 9.22271 14.9475 9.44229 14.85 9.6425ZM3.73311 11.7331C3.26444 12.2018 3.00079 12.8372 3 13.5V15H11V13.5C10.9992 12.8372 10.7356 12.2018 10.2669 11.7331C9.79822 11.2644 9.1628 11.0008 8.5 11H5.5C4.8372 11.0008 4.20178 11.2644 3.73311 11.7331Z" fill="currentColor"></path></svg></div>

	

	<span>Automatic Speech Recognition</span>
	

	</div></a>
	<a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=transformers"><div class="tag   tag-white "><svg class="text-black inline-block text-sm" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" width="1em" height="1em" viewBox="0 0 95 88"><path fill="#fff" d="M94.25 70.08a8.28 8.28 0 0 1-.43 6.46 10.57 10.57 0 0 1-3 3.6 25.18 25.18 0 0 1-5.7 3.2 65.74 65.74 0 0 1-7.56 2.65 46.67 46.67 0 0 1-11.42 1.68c-5.42.05-10.09-1.23-13.4-4.5a40.4 40.4 0 0 1-10.14.03c-3.34 3.25-7.99 4.52-13.39 4.47a46.82 46.82 0 0 1-11.43-1.68 66.37 66.37 0 0 1-7.55-2.65c-2.28-.98-4.17-2-5.68-3.2a10.5 10.5 0 0 1-3.02-3.6c-.99-2-1.18-4.3-.42-6.46a8.54 8.54 0 0 1-.33-5.63c.25-.95.66-1.83 1.18-2.61a8.67 8.67 0 0 1 2.1-8.47 8.23 8.23 0 0 1 2.82-2.07 41.75 41.75 0 1 1 81.3-.12 8.27 8.27 0 0 1 3.11 2.19 8.7 8.7 0 0 1 2.1 8.47c.52.78.93 1.66 1.18 2.61a8.61 8.61 0 0 1-.32 5.63Z"></path><path fill="#FFD21E" d="M47.21 76.5a34.75 34.75 0 1 0 0-69.5 34.75 34.75 0 0 0 0 69.5Z"></path><path fill="#FF9D0B" d="M81.96 41.75a34.75 34.75 0 1 0-69.5 0 34.75 34.75 0 0 0 69.5 0Zm-73.5 0a38.75 38.75 0 1 1 77.5 0 38.75 38.75 0 0 1-77.5 0Z"></path><path fill="#3A3B45" d="M58.5 32.3c1.28.44 1.78 3.06 3.07 2.38a5 5 0 1 0-6.76-2.07c.61 1.15 2.55-.72 3.7-.32ZM34.95 32.3c-1.28.44-1.79 3.06-3.07 2.38a5 5 0 1 1 6.76-2.07c-.61 1.15-2.56-.72-3.7-.32Z"></path><path fill="#FF323D" d="M46.96 56.29c9.83 0 13-8.76 13-13.26 0-2.34-1.57-1.6-4.09-.36-2.33 1.15-5.46 2.74-8.9 2.74-7.19 0-13-6.88-13-2.38s3.16 13.26 13 13.26Z"></path><path fill="#3A3B45" fill-rule="evenodd" d="M39.43 54a8.7 8.7 0 0 1 5.3-4.49c.4-.12.81.57 1.24 1.28.4.68.82 1.37 1.24 1.37.45 0 .9-.68 1.33-1.35.45-.7.89-1.38 1.32-1.25a8.61 8.61 0 0 1 5 4.17c3.73-2.94 5.1-7.74 5.1-10.7 0-2.34-1.57-1.6-4.09-.36l-.14.07c-2.31 1.15-5.39 2.67-8.77 2.67s-6.45-1.52-8.77-2.67c-2.6-1.29-4.23-2.1-4.23.29 0 3.05 1.46 8.06 5.47 10.97Z" clip-rule="evenodd"></path><path fill="#FF9D0B" d="M70.71 37a3.25 3.25 0 1 0 0-6.5 3.25 3.25 0 0 0 0 6.5ZM24.21 37a3.25 3.25 0 1 0 0-6.5 3.25 3.25 0 0 0 0 6.5ZM17.52 48c-1.62 0-3.06.66-4.07 1.87a5.97 5.97 0 0 0-1.33 3.76 7.1 7.1 0 0 0-1.94-.3c-1.55 0-2.95.59-3.94 1.66a5.8 5.8 0 0 0-.8 7 5.3 5.3 0 0 0-1.79 2.82c-.24.9-.48 2.8.8 4.74a5.22 5.22 0 0 0-.37 5.02c1.02 2.32 3.57 4.14 8.52 6.1 3.07 1.22 5.89 2 5.91 2.01a44.33 44.33 0 0 0 10.93 1.6c5.86 0 10.05-1.8 12.46-5.34 3.88-5.69 3.33-10.9-1.7-15.92-2.77-2.78-4.62-6.87-5-7.77-.78-2.66-2.84-5.62-6.25-5.62a5.7 5.7 0 0 0-4.6 2.46c-1-1.26-1.98-2.25-2.86-2.82A7.4 7.4 0 0 0 17.52 48Zm0 4c.51 0 1.14.22 1.82.65 2.14 1.36 6.25 8.43 7.76 11.18.5.92 1.37 1.31 2.14 1.31 1.55 0 2.75-1.53.15-3.48-3.92-2.93-2.55-7.72-.68-8.01.08-.02.17-.02.24-.02 1.7 0 2.45 2.93 2.45 2.93s2.2 5.52 5.98 9.3c3.77 3.77 3.97 6.8 1.22 10.83-1.88 2.75-5.47 3.58-9.16 3.58-3.81 0-7.73-.9-9.92-1.46-.11-.03-13.45-3.8-11.76-7 .28-.54.75-.76 1.34-.76 2.38 0 6.7 3.54 8.57 3.54.41 0 .7-.17.83-.6.79-2.85-12.06-4.05-10.98-8.17.2-.73.71-1.02 1.44-1.02 3.14 0 10.2 5.53 11.68 5.53.11 0 .2-.03.24-.1.74-1.2.33-2.04-4.9-5.2-5.21-3.16-8.88-5.06-6.8-7.33.24-.26.58-.38 1-.38 3.17 0 10.66 6.82 10.66 6.82s2.02 2.1 3.25 2.1c.28 0 .52-.1.68-.38.86-1.46-8.06-8.22-8.56-11.01-.34-1.9.24-2.85 1.31-2.85Z"></path><path fill="#FFD21E" d="M38.6 76.69c2.75-4.04 2.55-7.07-1.22-10.84-3.78-3.77-5.98-9.3-5.98-9.3s-.82-3.2-2.69-2.9c-1.87.3-3.24 5.08.68 8.01 3.91 2.93-.78 4.92-2.29 2.17-1.5-2.75-5.62-9.82-7.76-11.18-2.13-1.35-3.63-.6-3.13 2.2.5 2.79 9.43 9.55 8.56 11-.87 1.47-3.93-1.71-3.93-1.71s-9.57-8.71-11.66-6.44c-2.08 2.27 1.59 4.17 6.8 7.33 5.23 3.16 5.64 4 4.9 5.2-.75 1.2-12.28-8.53-13.36-4.4-1.08 4.11 11.77 5.3 10.98 8.15-.8 2.85-9.06-5.38-10.74-2.18-1.7 3.21 11.65 6.98 11.76 7.01 4.3 1.12 15.25 3.49 19.08-2.12Z"></path><path fill="#FF9D0B" d="M77.4 48c1.62 0 3.07.66 4.07 1.87a5.97 5.97 0 0 1 1.33 3.76 7.1 7.1 0 0 1 1.95-.3c1.55 0 2.95.59 3.94 1.66a5.8 5.8 0 0 1 .8 7 5.3 5.3 0 0 1 1.78 2.82c.24.9.48 2.8-.8 4.74a5.22 5.22 0 0 1 .37 5.02c-1.02 2.32-3.57 4.14-8.51 6.1-3.08 1.22-5.9 2-5.92 2.01a44.33 44.33 0 0 1-10.93 1.6c-5.86 0-10.05-1.8-12.46-5.34-3.88-5.69-3.33-10.9 1.7-15.92 2.78-2.78 4.63-6.87 5.01-7.77.78-2.66 2.83-5.62 6.24-5.62a5.7 5.7 0 0 1 4.6 2.46c1-1.26 1.98-2.25 2.87-2.82A7.4 7.4 0 0 1 77.4 48Zm0 4c-.51 0-1.13.22-1.82.65-2.13 1.36-6.25 8.43-7.76 11.18a2.43 2.43 0 0 1-2.14 1.31c-1.54 0-2.75-1.53-.14-3.48 3.91-2.93 2.54-7.72.67-8.01a1.54 1.54 0 0 0-.24-.02c-1.7 0-2.45 2.93-2.45 2.93s-2.2 5.52-5.97 9.3c-3.78 3.77-3.98 6.8-1.22 10.83 1.87 2.75 5.47 3.58 9.15 3.58 3.82 0 7.73-.9 9.93-1.46.1-.03 13.45-3.8 11.76-7-.29-.54-.75-.76-1.34-.76-2.38 0-6.71 3.54-8.57 3.54-.42 0-.71-.17-.83-.6-.8-2.85 12.05-4.05 10.97-8.17-.19-.73-.7-1.02-1.44-1.02-3.14 0-10.2 5.53-11.68 5.53-.1 0-.19-.03-.23-.1-.74-1.2-.34-2.04 4.88-5.2 5.23-3.16 8.9-5.06 6.8-7.33-.23-.26-.57-.38-.98-.38-3.18 0-10.67 6.82-10.67 6.82s-2.02 2.1-3.24 2.1a.74.74 0 0 1-.68-.38c-.87-1.46 8.05-8.22 8.55-11.01.34-1.9-.24-2.85-1.31-2.85Z"></path><path fill="#FFD21E" d="M56.33 76.69c-2.75-4.04-2.56-7.07 1.22-10.84 3.77-3.77 5.97-9.3 5.97-9.3s.82-3.2 2.7-2.9c1.86.3 3.23 5.08-.68 8.01-3.92 2.93.78 4.92 2.28 2.17 1.51-2.75 5.63-9.82 7.76-11.18 2.13-1.35 3.64-.6 3.13 2.2-.5 2.79-9.42 9.55-8.55 11 .86 1.47 3.92-1.71 3.92-1.71s9.58-8.71 11.66-6.44c2.08 2.27-1.58 4.17-6.8 7.33-5.23 3.16-5.63 4-4.9 5.2.75 1.2 12.28-8.53 13.36-4.4 1.08 4.11-11.76 5.3-10.97 8.15.8 2.85 9.05-5.38 10.74-2.18 1.69 3.21-11.65 6.98-11.76 7.01-4.31 1.12-15.26 3.49-19.08-2.12Z"></path></svg>

	

	<span>Transformers</span>
	

	</div></a>
	<a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=safetensors"><div class="tag   tag-white "><svg class="text-black inline-block text-sm" viewBox="0 0 57 44" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet"><path d="M36.816 20.1474L54.9918 27.4409C55.5142 27.6506 55.9623 28.0112 56.2788 28.4766C56.5954 28.9421 56.7661 29.4913 56.7691 30.0542C56.7722 30.6171 56.6074 31.1682 56.2959 31.637C55.9844 32.1059 55.5402 32.4713 55.0201 32.6866L29.953 43.0646C29.2593 43.3518 28.4799 43.3518 27.7862 43.0646L2.71624 32.6894C2.19613 32.4741 1.75197 32.1087 1.44044 31.6398C1.12892 31.171 0.964165 30.62 0.967204 30.057C0.970244 29.4941 1.14094 28.9449 1.45751 28.4794C1.77408 28.014 2.22216 27.6534 2.74456 27.4437L21.2404 20.0227C22.2997 19.5979 25.6477 20.8441 28.8682 20.8555C32.3096 20.8668 35.6292 19.6715 36.816 20.1474ZM11.3042 30.1119L28.8682 37.3828L46.435 30.1119L28.8682 23.0619L11.3042 30.1119ZM29.9247 0.388251L54.9918 10.4462C55.5142 10.6559 55.9623 11.0165 56.2788 11.482C56.5954 11.9474 56.7661 12.4967 56.7691 13.0596C56.7722 13.6225 56.6074 14.1735 56.2959 14.6424C55.9844 15.1112 55.5402 15.4766 55.0201 15.6919L29.953 26.07C29.2593 26.3572 28.4799 26.3572 27.7862 26.07L2.71624 15.6948C2.19613 15.4795 1.75197 15.1141 1.44044 14.6452C1.12892 14.1763 0.964165 13.6253 0.967204 13.0624C0.970244 12.4995 1.14094 11.9503 1.45751 11.4848C1.77408 11.0193 2.22216 10.6588 2.74456 10.4491L27.8117 0.388251C28.4896 0.1157 29.2467 0.1157 29.9247 0.388251ZM11.3042 13.1172L28.8682 20.3881L46.435 13.1172L28.8682 6.06729L11.3042 13.1172Z" fill="currentColor"></path></svg>

	

	<span>Safetensors</span>
	

	</div></a>
	<a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?other=wav2vec2_to_vit5_bottleneck"><div class="tag   tag-white ">

	

	<span>wav2vec2_to_vit5_bottleneck</span>
	

	</div></a>
	<a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?other=custom_code"><div class="tag   tag-white ">

	

	<span>custom_code</span>
	

	</div></a>

	<div class="relative inline-block ">
	<button class="group mr-1 mb-1 md:mr-1.5 md:mb-1.5  rounded-full rounded-br-none " type="button">
		<div slot="button"><div class="tag rounded-full  tag-white relative rounded-br-none pr-2.5">
		<svg class="-mr-1 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 12 12" preserveAspectRatio="xMidYMid meet" fill="none"><path fill="currentColor" fill-rule="evenodd" d="M8.007 1.814a1.176 1.176 0 0 0-.732-.266H3.088c-.64 0-1.153.512-1.153 1.152v6.803c0 .64.513 1.152 1.153 1.152h5.54c.632 0 1.144-.511 1.144-1.152V3.816c0-.338-.137-.658-.412-.887L8.007 1.814Zm-1.875 1.81c0 .695.55 1.253 1.244 1.253h.983a.567.567 0 0 1 .553.585v4.041c0 .165-.119.302-.283.302h-5.55c-.156 0-.275-.137-.275-.302V2.7a.284.284 0 0 1 .284-.301h2.468a.574.574 0 0 1 .434.19.567.567 0 0 1 .142.395v.64Z" clip-rule="evenodd" fill-opacity=".8"></path><path fill="currentColor" fill-opacity=".2" fill-rule="evenodd" d="M6.132 3.624c0 .695.55 1.253 1.244 1.253h.97a.567.567 0 0 1 .566.585v4.041c0 .165-.119.302-.283.302h-5.55c-.156 0-.275-.137-.275-.302V2.7a.284.284 0 0 1 .284-.301h2.468a.567.567 0 0 1 .576.585v.64Z" clip-rule="evenodd"></path></svg>

	

	<span class="-mr-2 text-gray-400">arxiv:</span>
		<span>1910.09700</span>
	

	<div class="border-br-gray-200 absolute bottom-0.5 right-0.5 h-1 w-1 border-[3px] border-l-transparent border-t-transparent border-b-gray-200 border-r-gray-200 group-hover:border-b-gray-400 group-hover:border-r-gray-400 dark:border-b-gray-700 dark:border-r-gray-700 group-hover:dark:border-b-gray-400 group-hover:dark:border-r-gray-400"></div></div></div>
		</button>
	
	
	</div></div>

		<div class="flex flex-col-reverse lg:flex-row lg:items-center lg:justify-between"><div class="-mb-px flex h-12 items-center overflow-x-auto overflow-y-hidden ">
	<a class="tab-alternate" href="/huypd1508/wav2vec2-t5-Vietnamese"><svg class="mr-1.5 text-gray-400 flex-none" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
	Model card
	

	
		</a><a class="tab-alternate active" href="/huypd1508/wav2vec2-t5-Vietnamese/tree/main"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M21 19h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-8h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0 4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M9 19a1 1 0 0 1-1-1V6a1 1 0 0 1 2 0v12a1 1 0 0 1-1 1zm-6-4.333a1 1 0 0 1-.64-1.769L3.438 12l-1.078-.898a1 1 0 0 1 1.28-1.538l2 1.667a1 1 0 0 1 0 1.538l-2 1.667a.999.999 0 0 1-.64.231z" fill="currentColor"></path></svg>
	<span class="xl:hidden">Files</span>
		<span class="hidden xl:inline">Files and versions</span>
	

	

<span class="inline-block "><span class="contents"><div slot="anchor" class="shadow-purple-500/10 ml-2 inline-flex -translate-y-px items-center gap-0.5 rounded-md border bg-white px-1 py-0.5 align-middle text-xs font-semibold leading-none text-gray-800 shadow-sm dark:border-gray-700 dark:bg-gradient-to-b dark:from-gray-925 dark:to-gray-925 dark:text-gray-300"><svg class="size-3 " xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 12 12"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.14 3.64 5.1 4.92 2.98 2.28h2.06l1.1 1.36Zm0 4.72-1.1 1.36H2.98l2.13-2.64 1.03 1.28Zm4.9 1.36L8.03 6l3-3.72H8.96L5.97 6l3 3.72h2.06Z" fill="#7875FF"></path><path d="M4.24 6 2.6 8.03.97 6 2.6 3.97 4.24 6Z" fill="#FF7F41" opacity="1"></path></svg>
						<span>xet</span>
					</div></span>
	</span>
		</a><a class="tab-alternate" href="/huypd1508/wav2vec2-t5-Vietnamese/discussions"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M20.6081 3C21.7684 3 22.8053 3.49196 23.5284 4.38415C23.9756 4.93678 24.4428 5.82749 24.4808 7.16133C24.9674 7.01707 25.4353 6.93643 25.8725 6.93643C26.9833 6.93643 27.9865 7.37587 28.696 8.17411C29.6075 9.19872 30.0124 10.4579 29.8361 11.7177C29.7523 12.3177 29.5581 12.8555 29.2678 13.3534C29.8798 13.8646 30.3306 14.5763 30.5485 15.4322C30.719 16.1032 30.8939 17.5006 29.9808 18.9403C30.0389 19.0342 30.0934 19.1319 30.1442 19.2318C30.6932 20.3074 30.7283 21.5229 30.2439 22.6548C29.5093 24.3704 27.6841 25.7219 24.1397 27.1727C21.9347 28.0753 19.9174 28.6523 19.8994 28.6575C16.9842 29.4379 14.3477 29.8345 12.0653 29.8345C7.87017 29.8345 4.8668 28.508 3.13831 25.8921C0.356375 21.6797 0.754104 17.8269 4.35369 14.1131C6.34591 12.058 7.67023 9.02782 7.94613 8.36275C8.50224 6.39343 9.97271 4.20438 12.4172 4.20438H12.4179C12.6236 4.20438 12.8314 4.2214 13.0364 4.25468C14.107 4.42854 15.0428 5.06476 15.7115 6.02205C16.4331 5.09583 17.134 4.359 17.7682 3.94323C18.7242 3.31737 19.6794 3 20.6081 3ZM20.6081 5.95917C20.2427 5.95917 19.7963 6.1197 19.3039 6.44225C17.7754 7.44319 14.8258 12.6772 13.7458 14.7131C13.3839 15.3952 12.7655 15.6837 12.2086 15.6837C11.1036 15.6837 10.2408 14.5497 12.1076 13.1085C14.9146 10.9402 13.9299 7.39584 12.5898 7.1776C12.5311 7.16799 12.4731 7.16355 12.4172 7.16355C11.1989 7.16355 10.6615 9.33114 10.6615 9.33114C10.6615 9.33114 9.0863 13.4148 6.38031 16.206C3.67434 18.998 3.5346 21.2388 5.50675 24.2246C6.85185 26.2606 9.42666 26.8753 12.0653 26.8753C14.8021 26.8753 17.6077 26.2139 19.1799 25.793C19.2574 25.7723 28.8193 22.984 27.6081 20.6107C27.4046 20.212 27.0693 20.0522 26.6471 20.0522C24.9416 20.0522 21.8393 22.6726 20.5057 22.6726C20.2076 22.6726 19.9976 22.5416 19.9116 22.222C19.3433 20.1173 28.552 19.2325 27.7758 16.1839C27.639 15.6445 27.2677 15.4256 26.746 15.4263C24.4923 15.4263 19.4358 19.5181 18.3759 19.5181C18.2949 19.5181 18.2368 19.4937 18.2053 19.4419C17.6743 18.557 17.9653 17.9394 21.7082 15.6009C25.4511 13.2617 28.0783 11.8545 26.5841 10.1752C26.4121 9.98141 26.1684 9.8956 25.8725 9.8956C23.6001 9.89634 18.2311 14.9403 18.2311 14.9403C18.2311 14.9403 16.7821 16.496 15.9057 16.496C15.7043 16.496 15.533 16.4139 15.4169 16.2112C14.7956 15.1296 21.1879 10.1286 21.5484 8.06535C21.7928 6.66715 21.3771 5.95917 20.6081 5.95917Z" fill="#FF9D00"></path><path d="M5.50686 24.2246C3.53472 21.2387 3.67446 18.9979 6.38043 16.206C9.08641 13.4147 10.6615 9.33111 10.6615 9.33111C10.6615 9.33111 11.2499 6.95933 12.59 7.17757C13.93 7.39581 14.9139 10.9401 12.1069 13.1084C9.29997 15.276 12.6659 16.7489 13.7459 14.713C14.8258 12.6772 17.7747 7.44316 19.304 6.44221C20.8326 5.44128 21.9089 6.00204 21.5484 8.06532C21.188 10.1286 14.795 15.1295 15.4171 16.2118C16.0391 17.2934 18.2312 14.9402 18.2312 14.9402C18.2312 14.9402 25.0907 8.49588 26.5842 10.1752C28.0776 11.8545 25.4512 13.2616 21.7082 15.6008C17.9646 17.9393 17.6744 18.557 18.2054 19.4418C18.7372 20.3266 26.9998 13.1351 27.7759 16.1838C28.5513 19.2324 19.3434 20.1173 19.9117 22.2219C20.48 24.3274 26.3979 18.2382 27.6082 20.6107C28.8193 22.9839 19.2574 25.7722 19.18 25.7929C16.0914 26.62 8.24723 28.3726 5.50686 24.2246Z" fill="#FFD21E"></path></svg>
	Community
	

	
		</a><a class="tab-alternate" href="/huypd1508/wav2vec2-t5-Vietnamese/settings"><svg class="opacity-50 dark:opacity-70 mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25" fill="currentColor"><path d="M13.0101 3C13.7157 3.0078 14.4184 3.09062 15.1077 3.24652C15.2543 3.2797 15.3871 3.35848 15.4874 3.47186C15.5877 3.58523 15.6506 3.72754 15.6672 3.8789L15.8306 5.36678C15.8537 5.57655 15.925 5.77791 16.0389 5.95464C16.1527 6.13137 16.3059 6.27854 16.4861 6.38432C16.6663 6.4901 16.8685 6.55153 17.0764 6.56367C17.2843 6.57581 17.4921 6.53831 17.6831 6.4542L19.0299 5.85495C19.1667 5.79391 19.3187 5.77743 19.4651 5.8078C19.6115 5.83818 19.745 5.9139 19.847 6.02449C20.8199 7.07789 21.5443 8.3412 21.9658 9.71937C22.01 9.8642 22.0087 10.0194 21.962 10.1634C21.9153 10.3074 21.8256 10.4332 21.7053 10.5232L20.5113 11.4158C20.3434 11.5408 20.2069 11.7041 20.1128 11.8925C20.0187 12.0809 19.9697 12.2891 19.9697 12.5003C19.9697 12.7114 20.0187 12.9196 20.1128 13.108C20.2069 13.2964 20.3434 13.4597 20.5113 13.5848L21.7062 14.4763C21.8269 14.5663 21.917 14.6922 21.9638 14.8364C22.0107 14.9806 22.0121 15.1361 21.9677 15.2812C21.546 16.6593 20.8216 17.9225 19.849 18.976C19.7471 19.0864 19.6141 19.162 19.4681 19.1926C19.3221 19.2231 19.1704 19.207 19.0338 19.1466L17.6812 18.5454C17.4904 18.4606 17.2827 18.4225 17.0748 18.4343C16.8668 18.446 16.6645 18.5072 16.4842 18.6129C16.3039 18.7185 16.1508 18.8658 16.037 19.0426C15.9233 19.2195 15.8523 19.421 15.8297 19.6308L15.6672 21.1177C15.6508 21.2674 15.5892 21.4084 15.4908 21.5212C15.3923 21.6341 15.2619 21.7133 15.1173 21.7482C13.7249 22.0839 12.2742 22.0839 10.8817 21.7482C10.7371 21.7133 10.6067 21.6341 10.5083 21.5212C10.4098 21.4084 10.3482 21.2674 10.3318 21.1177L10.1703 19.6328C10.1468 19.4235 10.0751 19.2227 9.96107 19.0465C9.84703 18.8704 9.69381 18.7238 9.51373 18.6186C9.33364 18.5134 9.13172 18.4525 8.92419 18.4408C8.71666 18.4291 8.50931 18.4669 8.31882 18.5512L6.9672 19.1514C6.83048 19.2121 6.67854 19.2283 6.53235 19.1978C6.38616 19.1672 6.25292 19.0915 6.15103 18.9809C5.17789 17.9263 4.45346 16.6616 4.03227 15.2821C3.98795 15.1371 3.98931 14.9816 4.03617 14.8374C4.08304 14.6931 4.17306 14.5673 4.29375 14.4773L5.48868 13.5848C5.65676 13.4599 5.79345 13.2966 5.88768 13.1082C5.9819 12.9198 6.031 12.7115 6.031 12.5003C6.031 12.289 5.9819 12.0808 5.88768 11.8923C5.79345 11.7039 5.65676 11.5407 5.48868 11.4158L4.29375 10.5252C4.17324 10.4351 4.0834 10.3092 4.03671 10.1649C3.99003 10.0207 3.98881 9.8653 4.03323 9.72034C4.45479 8.34219 5.17922 7.07889 6.15199 6.02547C6.25407 5.91487 6.38753 5.83915 6.53391 5.80878C6.6803 5.77841 6.83238 5.79488 6.96912 5.85593L8.31498 6.45517C8.5063 6.53923 8.71441 6.57664 8.92258 6.56439C9.13075 6.55214 9.33319 6.49057 9.51363 6.38462C9.69406 6.27868 9.84747 6.13132 9.96152 5.95438C10.0756 5.77744 10.1471 5.57585 10.1703 5.36581L10.3338 3.8789C10.3503 3.72724 10.4132 3.58462 10.5137 3.47103C10.6142 3.35745 10.7473 3.2786 10.8942 3.24555C11.5835 3.09062 12.2881 3.00877 13.0101 3ZM12.9986 9.57711C12.2337 9.57711 11.5001 9.88508 10.9593 10.4333C10.4184 10.9815 10.1146 11.725 10.1146 12.5003C10.1146 13.2755 10.4184 14.0191 10.9593 14.5672C11.5001 15.1154 12.2337 15.4234 12.9986 15.4234C13.7634 15.4234 14.497 15.1154 15.0378 14.5672C15.5787 14.0191 15.8825 13.2755 15.8825 12.5003C15.8825 11.725 15.5787 10.9815 15.0378 10.4333C14.497 9.88508 13.7634 9.57711 12.9986 9.57711Z"></path></svg>
	Settings
	

	
		</a></div>
	
			


<div class="relative mb-1.5 flex flex-wrap gap-1.5 sm:flex-nowrap lg:mb-0"><div class="order-last sm:order-first"><div class="relative ">
	<button class="btn px-1.5 py-1.5 " type="button">
		
			<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="p-0.5" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><circle cx="16" cy="7" r="3" fill="currentColor"></circle><circle cx="16" cy="16" r="3" fill="currentColor"></circle><circle cx="16" cy="25" r="3" fill="currentColor"></circle></svg>
		
		</button>
	
	
	</div></div>














	<div class="flex-none w-full sm:w-auto"><div class="relative ">
	<button class="text-sm btn btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><rect x="6.34" y="19" width="11.31" height="2" transform="translate(-10.63 14.34) rotate(-45)"></rect><path d="M17,30a1,1,0,0,1-.37-.07,1,1,0,0,1-.62-.79l-1-7,2-.28.75,5.27L21,24.52V17a1,1,0,0,1,.29-.71l4.07-4.07A8.94,8.94,0,0,0,28,5.86V4H26.14a8.94,8.94,0,0,0-6.36,2.64l-4.07,4.07A1,1,0,0,1,15,11H7.48L4.87,14.26l5.27.75-.28,2-7-1a1,1,0,0,1-.79-.62,1,1,0,0,1,.15-1l4-5A1,1,0,0,1,7,9h7.59l3.77-3.78A10.92,10.92,0,0,1,26.14,2H28a2,2,0,0,1,2,2V5.86a10.92,10.92,0,0,1-3.22,7.78L23,17.41V25a1,1,0,0,1-.38.78l-5,4A1,1,0,0,1,17,30Z"></path></svg>
			Deploy
		<svg class="-mr-1 text-gray-500 " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div>

		

		

		
		

		

		</div>
		<div class="relative flex-auto sm:flex-none">
	<button class="from-gray-800! to-black! text-white! gap-1! border-gray-800! dark:border-gray-900!  btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 mr-0.5! " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M28 4H4a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h8v4H8v2h16v-2h-4v-4h8a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2ZM18 28h-4v-4h4Zm10-6H4V6h24Z"></path></svg>
			Use this model
		<svg class="-mr-1 text-gray-500 " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div>



</div>
	</div></div></header>
</div>
	
<div class="container relative flex flex-col md:grid md:space-y-0 w-full md:grid-cols-12  space-y-4 md:gap-6 mb-16"><section class="pt-8 border-gray-100 col-span-full"><div class="SVELTE_HYDRATER contents" data-target="ViewerHeader" data-props="{&quot;authLight&quot;:{&quot;csrfToken&quot;:&quot;eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3NjU4MTAxMDA5OTIsInVzZXJJZCI6IjY2ZjYwYTVlODExYmI0ZTkzN2Y0ZTM0NSJ9LCJzaWduYXR1cmUiOiIwODU2MWE4NjFjZDFhNDNiZjI4MjE5ZGY5MGI3MWEzZWVlM2FlZjhkYmNiMzFlMDQzM2RiMjdlNWE2YTI4NmNhIn0=&quot;,&quot;hasHfLevelAccess&quot;:false,&quot;u&quot;:{&quot;avatarUrl&quot;:&quot;/avatars/16a7825f33635ba39f10147b19754fb6.svg&quot;,&quot;isPro&quot;:false,&quot;orgs&quot;:[],&quot;user&quot;:&quot;huypd1508&quot;,&quot;canPost&quot;:false,&quot;canHaveBilling&quot;:true,&quot;canCreateOrg&quot;:true,&quot;theme&quot;:&quot;system&quot;,&quot;notifications&quot;:{&quot;org_suggestions&quot;:false},&quot;hardwareItems&quot;:[],&quot;hardwareItemsPrivate&quot;:false,&quot;usage&quot;:{&quot;storage&quot;:{&quot;summary&quot;:{&quot;space&quot;:{&quot;used&quot;:0,&quot;usedPrivate&quot;:0,&quot;usedPublic&quot;:0,&quot;count&quot;:1},&quot;model&quot;:{&quot;used&quot;:36856368131,&quot;usedPrivate&quot;:0,&quot;usedPublic&quot;:36856368131,&quot;count&quot;:11}},&quot;used&quot;:36856368131,&quot;count&quot;:12,&quot;usedPrivate&quot;:0,&quot;usedPublic&quot;:36856368131},&quot;inference&quot;:{&quot;usedNanoUsd&quot;:0,&quot;numRequests&quot;:0,&quot;providerDetails&quot;:[],&quot;periodEnd&quot;:&quot;2025-12-31T23:59:59.999Z&quot;,&quot;periodStart&quot;:&quot;2025-12-01T00:00:00.000Z&quot;,&quot;includedNanoUsd&quot;:100000000,&quot;limitNanoUsd&quot;:100000000,&quot;lastUpdated&quot;:&quot;2025-12-14T14:48:17.984Z&quot;},&quot;zeroGpu&quot;:{&quot;base&quot;:210,&quot;current&quot;:210,&quot;lastUpdated&quot;:&quot;2025-12-14T14:48:17.984Z&quot;}},&quot;welcomeLinks&quot;:[],&quot;hasProOrOrgPaidPlan&quot;:false}},&quot;context&quot;:{&quot;repo&quot;:{&quot;name&quot;:&quot;huypd1508/wav2vec2-t5-Vietnamese&quot;,&quot;type&quot;:&quot;model&quot;},&quot;rev&quot;:&quot;main&quot;,&quot;path&quot;:&quot;modeling_wav2vec2_to_vit5_bottleneck.py&quot;,&quot;subpaths&quot;:[{&quot;dir&quot;:&quot;modeling_wav2vec2_to_vit5_bottleneck.py&quot;}]},&quot;refs&quot;:{&quot;branches&quot;:[{&quot;name&quot;:&quot;main&quot;,&quot;ref&quot;:&quot;refs/heads/main&quot;,&quot;targetCommit&quot;:&quot;fd0a116742837783784dd28b2bbd6b9defe491ab&quot;}],&quot;tags&quot;:[],&quot;converts&quot;:[]},&quot;view&quot;:&quot;blob&quot;,&quot;isMac&quot;:false}"><header class="flex flex-wrap items-center justify-start pb-2 md:justify-end lg:flex-nowrap"><div class="grow max-md:flex max-md:w-full max-md:items-start max-md:justify-between"><div class="relative mr-4 flex min-w-0 basis-auto flex-wrap items-center gap-x-3 md:grow md:basis-full lg:basis-auto lg:flex-nowrap"><div class="relative mb-2">
	<button class="text-sm md:text-base btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 text-gray-700 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M13 14c-3.36 0-4.46 1.35-4.82 2.24C9.25 16.7 10 17.76 10 19a3 3 0 0 1-3 3a3 3 0 0 1-3-3c0-1.31.83-2.42 2-2.83V7.83A2.99 2.99 0 0 1 4 5a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.31-.83 2.42-2 2.83v5.29c.88-.65 2.16-1.12 4-1.12c2.67 0 3.56-1.34 3.85-2.23A3.006 3.006 0 0 1 14 7a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.34-.88 2.5-2.09 2.86C17.65 11.29 16.68 14 13 14m-6 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1M7 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1m10 2a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1z" fill="currentColor"></path></svg>
			main
		<svg class="-mr-1 text-gray-500 " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div>
			<div class="relative mb-2 flex flex-wrap items-center"><a class="truncate text-gray-800 hover:underline" href="/huypd1508/wav2vec2-t5-Vietnamese/tree/main">wav2vec2-t5-Vietnamese</a>
				<span class="mx-1 text-gray-300">/</span>
					<span class="dark:text-gray-300">modeling_wav2vec2_to_vit5_bottleneck.py</span>
					<button class="text-xs ml-2 focus:outline-hidden inline-flex cursor-pointer items-center text-sm  mx-0.5   text-gray-600 " title="Copy path" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
		</button></div>
			</div>
		</div>
	
	</header></div>
			<div class="SVELTE_HYDRATER contents" data-target="LastCommit" data-props="{&quot;commitLast&quot;:{&quot;date&quot;:&quot;2025-12-14T02:41:54.000Z&quot;,&quot;verified&quot;:&quot;verified&quot;,&quot;subject&quot;:&quot;Update modeling_wav2vec2_to_vit5_bottleneck.py&quot;,&quot;authors&quot;:[{&quot;_id&quot;:&quot;66f60a5e811bb4e937f4e345&quot;,&quot;avatar&quot;:&quot;/avatars/16a7825f33635ba39f10147b19754fb6.svg&quot;,&quot;isHf&quot;:false,&quot;user&quot;:&quot;huypd1508&quot;}],&quot;commit&quot;:{&quot;id&quot;:&quot;fd0a116742837783784dd28b2bbd6b9defe491ab&quot;,&quot;parentIds&quot;:[&quot;9ae35786debf11e51a3ebe6a38e6e96855331f00&quot;]},&quot;title&quot;:&quot;Update modeling_wav2vec2_to_vit5_bottleneck.py&quot;},&quot;repo&quot;:{&quot;name&quot;:&quot;huypd1508/wav2vec2-t5-Vietnamese&quot;,&quot;type&quot;:&quot;model&quot;}}"><div class="from-gray-100-to-white bg-linear-to-t flex flex-wrap items-baseline gap-y-1 rounded-t-lg border border-b-0 px-3 py-2 dark:border-gray-800"><img class="mr-2.5 mt-0.5 h-4 w-4 self-center rounded-full" alt="huypd1508's picture" src="/avatars/16a7825f33635ba39f10147b19754fb6.svg">
			<div class="mr-4 flex flex-none items-center truncate"><a class="hover:underline" href="/huypd1508">huypd1508
					</a>
				
			</div>
		<div class="mr-4 truncate font-mono text-xs text-gray-500 hover:prose-a:underline sm:text-sm"><!-- HTML_TAG_START -->Update modeling_wav2vec2_to_vit5_bottleneck.py<!-- HTML_TAG_END --></div>
		<a class="rounded-sm border bg-gray-50 px-1.5 text-sm hover:underline dark:border-gray-800 dark:bg-gray-900" href="/huypd1508/wav2vec2-t5-Vietnamese/commit/fd0a116742837783784dd28b2bbd6b9defe491ab">fd0a116</a>
		<span class="mx-2 text-green-500 dark:text-green-600 px-1.5 border-green-100 dark:border-green-800 rounded-full border text-xs uppercase" title="This commit is signed and the signature is verified">verified</span>
		<time class="ml-auto hidden flex-none truncate pl-2 text-gray-500 dark:text-gray-400 lg:block" datetime="2025-12-14T02:41:54" title="Sun, 14 Dec 2025 02:41:54 GMT">about 12 hours ago</time></div></div>
			<div class="relative flex flex-wrap items-center border px-3 py-1.5 text-sm text-gray-800 dark:border-gray-800 dark:bg-gray-900 ">
				<a class="group my-1 mr-4 flex items-center " href="/huypd1508/wav2vec2-t5-Vietnamese/raw/main/modeling_wav2vec2_to_vit5_bottleneck.py"><span class="flex items-center group-hover:underline"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M31 16l-7 7l-1.41-1.41L28.17 16l-5.58-5.59L24 9l7 7z" fill="currentColor"></path><path d="M1 16l7-7l1.41 1.41L3.83 16l5.58 5.59L8 23l-7-7z" fill="currentColor"></path><path d="M12.419 25.484L17.639 6l1.932.518L14.35 26z" fill="currentColor"></path></svg>
								raw</span>
							
						</a><div class="SVELTE_HYDRATER contents" data-target="CopyButton" data-props="{&quot;value&quot;:&quot;https://huggingface.co/huypd1508/wav2vec2-t5-Vietnamese/resolve/main/modeling_wav2vec2_to_vit5_bottleneck.py&quot;,&quot;style&quot;:&quot;blank&quot;,&quot;label&quot;:&quot;Copy download link&quot;,&quot;classNames&quot;:&quot;my-1 mr-4 flex items-center no-underline hover:underline&quot;}"><button class="my-1 mr-4 flex items-center no-underline hover:underline       " title="Copy download link" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
		<span class="ml-1.5 ">Copy download link</span></button></div><a class="group my-1 mr-4 flex items-center " href="/huypd1508/wav2vec2-t5-Vietnamese/commits/main/modeling_wav2vec2_to_vit5_bottleneck.py"><span class="flex items-center group-hover:underline"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 4C9.383 4 4 9.383 4 16s5.383 12 12 12s12-5.383 12-12S22.617 4 16 4zm0 2c5.535 0 10 4.465 10 10s-4.465 10-10 10S6 21.535 6 16S10.465 6 16 6zm-1 2v9h7v-2h-5V8z" fill="currentColor"></path></svg>
								history</span>
							
						</a><a class="group my-1 mr-4 flex items-center " href="/huypd1508/wav2vec2-t5-Vietnamese/blame/main/modeling_wav2vec2_to_vit5_bottleneck.py"><span class="flex items-center group-hover:underline"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12a12 12 0 0 1-12 12z" fill="currentColor"></path><path d="M11.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path><path d="M20.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path></svg>
								blame</span>
							
						</a><a class="group my-1 mr-4 flex items-center " href="/huypd1508/wav2vec2-t5-Vietnamese/edit/main/modeling_wav2vec2_to_vit5_bottleneck.py"><span class="flex items-center group-hover:underline"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M2 26h28v2H2z" fill="currentColor"></path><path d="M25.4 9c.8-.8.8-2 0-2.8l-3.6-3.6c-.8-.8-2-.8-2.8 0l-15 15V24h6.4l15-15zm-5-5L24 7.6l-3 3L17.4 7l3-3zM6 22v-3.6l10-10l3.6 3.6l-10 10H6z" fill="currentColor"></path></svg>
								edit</span>
							
						</a><a class="group my-1 mr-4 flex items-center " href="/huypd1508/wav2vec2-t5-Vietnamese/delete/main/modeling_wav2vec2_to_vit5_bottleneck.py"><span class="flex items-center group-hover:underline"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M12 12h2v12h-2z" fill="currentColor"></path><path d="M18 12h2v12h-2z" fill="currentColor"></path><path d="M4 6v2h2v20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8h2V6zm4 22V8h16v20z" fill="currentColor"></path><path d="M12 2h8v2h-8z" fill="currentColor"></path></svg>
								delete</span>
							
						</a>

				<div class="mr-4 flex items-center"><div class="SVELTE_HYDRATER contents" data-target="ScanStatusBadge" data-props="{&quot;classNames&quot;:&quot;mr-2&quot;,&quot;scanStatus&quot;:{&quot;status&quot;:&quot;queued&quot;,&quot;protectAiScan&quot;:{&quot;status&quot;:&quot;unscanned&quot;,&quot;message&quot;:null,&quot;reportLink&quot;:&quot;https://protectai.com/insights/models/huypd1508/wav2vec2-t5-Vietnamese/fd0a116742837783784dd28b2bbd6b9defe491ab/files?blob-id=a392490b2f364b05b749dcd88456f588682543c3&amp;utm_source=huggingface&quot;},&quot;avScan&quot;:{&quot;status&quot;:&quot;safe&quot;,&quot;message&quot;:&quot;No security issues detected&quot;,&quot;reportLink&quot;:&quot;https://fdtn.ai/ai-supply-chain/hugging-face?utm_source=huggingface&quot;,&quot;reportLabel&quot;:&quot;Learn more at Cisco Foundation AI&quot;},&quot;pickleImportScan&quot;:{&quot;status&quot;:&quot;unscanned&quot;,&quot;pickleImports&quot;:[],&quot;version&quot;:&quot;0.0.0&quot;},&quot;virusTotalScan&quot;:{&quot;status&quot;:&quot;unscanned&quot;},&quot;jFrogScan&quot;:{&quot;status&quot;:&quot;queued&quot;,&quot;message&quot;:&quot;&quot;,&quot;reportLink&quot;:&quot;&quot;,&quot;reportLabel&quot;:&quot;&quot;}},&quot;repo&quot;:{&quot;name&quot;:&quot;huypd1508/wav2vec2-t5-Vietnamese&quot;,&quot;type&quot;:&quot;model&quot;},&quot;revision&quot;:&quot;main&quot;,&quot;filePath&quot;:&quot;modeling_wav2vec2_to_vit5_bottleneck.py&quot;,&quot;openByDefault&quot;:false}"><div class="sm:relative mr-2"><button class="flex h-[1.125rem] select-none items-center gap-0.5 rounded border pl-0.5 pr-0.5 text-xs leading-tight text-gray-400 hover:cursor-pointer text-gray-400 hover:border-gray-200 hover:bg-gray-50 hover:text-gray-500 dark:border-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200 "><svg class="flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 26" fill="none"><path fill="currentColor" fill-opacity=".67" d="M12.324 12.04a2.038 2.038 0 0 0-2.033 2.033c0 1.118.915 2.033 2.033 2.033a2.038 2.038 0 0 0 2.032-2.033 2.038 2.038 0 0 0-2.032-2.032Zm6.097 2.033a6.102 6.102 0 0 0-6.097-6.097 6.102 6.102 0 0 0-6.098 6.097 6.094 6.094 0 0 0 3.049 5.274l1.016-1.768c-1.21-.711-2.032-2.002-2.032-3.506a4.064 4.064 0 0 1 4.065-4.065 4.064 4.064 0 0 1 4.065 4.065c0 1.504-.823 2.795-2.033 3.506l1.017 1.768a6.094 6.094 0 0 0 3.048-5.274ZM12.324 3.911C6.714 3.91 2.16 8.463 2.16 14.073c0 3.76 2.043 7.033 5.071 8.79l1.016-1.757c-2.418-1.413-4.054-4.025-4.054-7.033a8.128 8.128 0 0 1 8.13-8.13 8.128 8.128 0 0 1 8.13 8.13c0 3.008-1.636 5.62-4.065 7.033l1.016 1.758c3.039-1.758 5.081-5.03 5.081-8.79 0-5.61-4.553-10.163-10.162-10.163Z"></path><path fill="url(#icon-scan-queued-a)" d="m4.197 9.392 8.113 4.683-2.508-8.939-5.605 4.256Z"></path><defs><linearGradient id="icon-scan-queued-a" x1="11.957" x2="6.965" y1="13.453" y2="7.399" gradientUnits="userSpaceOnUse"><stop stop-color="#AEB6C2"></stop><stop offset="1" stop-color="#D1D5DB" stop-opacity="0"></stop></linearGradient></defs></svg></button>

	</div></div>
						</div>

				<div class="flex items-center gap-x-3 dark:text-gray-300 sm:ml-auto"><div class="SVELTE_HYDRATER contents" data-target="LineWrapButton" data-props="{&quot;classNames&quot;:&quot;text-xs&quot;,&quot;lineSelectorClass&quot;:&quot;blob-line&quot;}">

<button class="text-xs focus:outline-hidden inline-flex cursor-pointer items-center justify-center text-sm  mx-0.5  " type="button"><svg class="opacity-40" width="1em" height="1em" viewBox="0 0 12 11" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M0.75 1.25H11.25M0.75 5H9C9.75 5 11.25 5.375 11.25 6.875C11.25 8.375 9.99975 8.75 9.375 8.75H6M6 8.75L7.5 7.25M6 8.75L7.5 10.25M0.75 8.75H3.75" stroke="currentColor" stroke-width="1.125" stroke-linecap="round" stroke-linejoin="round"></path></svg></button></div>
					5.59 kB</div></div>

			<div class="relative min-h-[100px] rounded-b-lg border border-t-0 leading-tight dark:border-gray-800 dark:bg-gray-925">
				<div class="py-3"><div class="SVELTE_HYDRATER contents" data-target="BlobContent" data-props="{&quot;lines&quot;:[&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> torch&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> torch.nn <span class=\&quot;hljs-keyword\&quot;>as</span> nn&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> transformers <span class=\&quot;hljs-keyword\&quot;>import</span> PreTrainedModel, Wav2Vec2Model, AutoModelForSeq2SeqLM&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> transformers.modeling_outputs <span class=\&quot;hljs-keyword\&quot;>import</span> BaseModelOutput&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> .configuration_wav2vec2_to_vit5_bottleneck <span class=\&quot;hljs-keyword\&quot;>import</span> Wav2Vec2ToVit5BottleneckConfig&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>class</span> <span class=\&quot;hljs-title class_\&quot;>BottleneckAdapter</span>(nn.Module):&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>__init__</span>(<span class=\&quot;hljs-params\&quot;>self, input_dim, output_dim, num_layers=<span class=\&quot;hljs-number\&quot;>2</span>, num_heads=<span class=\&quot;hljs-number\&quot;>4</span>, bottleneck_dim=<span class=\&quot;hljs-number\&quot;>256</span></span>):&quot;,&quot;        <span class=\&quot;hljs-built_in\&quot;>super</span>().__init__()&quot;,&quot;        encoder_layer = nn.TransformerEncoderLayer(&quot;,&quot;            d_model=bottleneck_dim,&quot;,&quot;            nhead=num_heads,&quot;,&quot;            dim_feedforward=<span class=\&quot;hljs-number\&quot;>1024</span>,&quot;,&quot;            dropout=<span class=\&quot;hljs-number\&quot;>0.1</span>,&quot;,&quot;            activation=<span class=\&quot;hljs-string\&quot;>&amp;quot;gelu&amp;quot;</span>,&quot;,&quot;            batch_first=<span class=\&quot;hljs-literal\&quot;>True</span>&quot;,&quot;        )&quot;,&quot;        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)&quot;,&quot;        self.bottleneck_proj = nn.Linear(input_dim, bottleneck_dim)&quot;,&quot;        self.output_proj = nn.Linear(bottleneck_dim, output_dim)&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>forward</span>(<span class=\&quot;hljs-params\&quot;>self, x, src_key_padding_mask=<span class=\&quot;hljs-literal\&quot;>None</span></span>):&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Project to bottleneck</span>&quot;,&quot;        x = self.bottleneck_proj(x)      &quot;,&quot;        x = self.encoder(x, src_key_padding_mask=src_key_padding_mask)&quot;,&quot;        x = self.output_proj(x)          &quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> x&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>class</span> <span class=\&quot;hljs-title class_\&quot;>Wav2Vec2ToVit5WithAdapter</span>(<span class=\&quot;hljs-title class_ inherited__\&quot;>PreTrainedModel</span>):&quot;,&quot;    config_class = Wav2Vec2ToVit5BottleneckConfig&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>__init__</span>(<span class=\&quot;hljs-params\&quot;>self, config</span>):&quot;,&quot;        <span class=\&quot;hljs-built_in\&quot;>super</span>().__init__(config)&quot;,&quot;        self.encoder = Wav2Vec2Model.from_pretrained(config.encoder_model_name)&quot;,&quot;        self.decoder = AutoModelForSeq2SeqLM.from_pretrained(config.decoder_model_name)&quot;,&quot;        self.adapter = BottleneckAdapter(&quot;,&quot;            input_dim=self.encoder.config.hidden_size,&quot;,&quot;            output_dim=self.decoder.config.d_model,&quot;,&quot;            num_layers=config.num_layers,&quot;,&quot;            num_heads=config.num_heads,&quot;,&quot;            bottleneck_dim=config.bottleneck_dim&quot;,&quot;        )&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>enable_input_require_grads</span>(<span class=\&quot;hljs-params\&quot;>self</span>):&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> &quot;,&quot;        &quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>get_input_embeddings</span>(<span class=\&quot;hljs-params\&quot;>self</span>):&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> self.decoder.get_input_embeddings()&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>set_input_embeddings</span>(<span class=\&quot;hljs-params\&quot;>self, value</span>):&quot;,&quot;        self.decoder.set_input_embeddings(value)&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>forward</span>(<span class=\&quot;hljs-params\&quot;>self, input_values=<span class=\&quot;hljs-literal\&quot;>None</span>, attention_mask=<span class=\&quot;hljs-literal\&quot;>None</span>, decoder_input_ids=<span class=\&quot;hljs-literal\&quot;>None</span>, labels=<span class=\&quot;hljs-literal\&quot;>None</span>, **kwargs</span>):&quot;,&quot;        encoder_outputs = self.encoder(input_values=input_values, attention_mask=attention_mask)&quot;,&quot;        hidden_states = encoder_outputs.last_hidden_state   <span class=\&quot;hljs-comment\&quot;># Get last hidden_state from encoder outputs</span>&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> self.training:                      <span class=\&quot;hljs-comment\&quot;># Fix for gradient checkpointing</span>&quot;,&quot;            hidden_states.requires_grad_(<span class=\&quot;hljs-literal\&quot;>True</span>)&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> hidden_states.grad_fn <span class=\&quot;hljs-keyword\&quot;>is</span> <span class=\&quot;hljs-literal\&quot;>None</span>:&quot;,&quot;                hidden_states.retain_grad()&quot;,&quot;&quot;,&quot;        &quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> attention_mask <span class=\&quot;hljs-keyword\&quot;>is</span> <span class=\&quot;hljs-keyword\&quot;>not</span> <span class=\&quot;hljs-literal\&quot;>None</span>:        <span class=\&quot;hljs-comment\&quot;># Get attention_mask that matched with last hidden_state size</span>&quot;,&quot;            &quot;,&quot;            output_lengths = self.encoder._get_feat_extract_output_lengths(attention_mask.<span class=\&quot;hljs-built_in\&quot;>sum</span>(-<span class=\&quot;hljs-number\&quot;>1</span>))&quot;,&quot;    &quot;,&quot;            batch_size, max_length = hidden_states.shape[:<span class=\&quot;hljs-number\&quot;>2</span>]&quot;,&quot;            encoder_attention_mask = torch.zeros(&quot;,&quot;                (batch_size, max_length), dtype=torch.<span class=\&quot;hljs-built_in\&quot;>bool</span>, device=hidden_states.device&quot;,&quot;            )&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>for</span> i, length <span class=\&quot;hljs-keyword\&quot;>in</span> <span class=\&quot;hljs-built_in\&quot;>enumerate</span>(output_lengths):&quot;,&quot;                encoder_attention_mask[i, :length] = <span class=\&quot;hljs-literal\&quot;>True</span>&quot;,&quot;            encoder_padding_mask = ~encoder_attention_mask  &quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>else</span>:&quot;,&quot;            encoder_padding_mask = torch.zeros_like(hidden_states[..., <span class=\&quot;hljs-number\&quot;>0</span>], dtype=torch.<span class=\&quot;hljs-built_in\&quot;>bool</span>)&quot;,&quot;            encoder_attention_mask = torch.ones_like(hidden_states[..., <span class=\&quot;hljs-number\&quot;>0</span>], dtype=torch.<span class=\&quot;hljs-built_in\&quot;>bool</span>)&quot;,&quot;&quot;,&quot;        adapted_states = self.adapter(hidden_states, src_key_padding_mask=encoder_padding_mask) <span class=\&quot;hljs-comment\&quot;># Adapter Output</span>&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Here we call the T5 model, but only use the decoder by passing adapter output to encoder_outputs</span>&quot;,&quot;        outputs = self.decoder(&quot;,&quot;            encoder_outputs=BaseModelOutput(last_hidden_state=adapted_states),&quot;,&quot;            attention_mask=encoder_attention_mask,&quot;,&quot;            decoder_input_ids=decoder_input_ids,&quot;,&quot;            labels=labels,&quot;,&quot;            return_dict=<span class=\&quot;hljs-literal\&quot;>True</span>&quot;,&quot;        )&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> {&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>&amp;quot;loss&amp;quot;</span>: outputs.loss.unsqueeze(<span class=\&quot;hljs-number\&quot;>0</span>) <span class=\&quot;hljs-keyword\&quot;>if</span> outputs.loss <span class=\&quot;hljs-keyword\&quot;>is</span> <span class=\&quot;hljs-keyword\&quot;>not</span> <span class=\&quot;hljs-literal\&quot;>None</span> <span class=\&quot;hljs-keyword\&quot;>else</span> <span class=\&quot;hljs-literal\&quot;>None</span>,&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>&amp;quot;logits&amp;quot;</span>: outputs.logits&quot;,&quot;        }&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>generate</span>(<span class=\&quot;hljs-params\&quot;>self, input_values=<span class=\&quot;hljs-literal\&quot;>None</span>, attention_mask=<span class=\&quot;hljs-literal\&quot;>None</span>, max_length=<span class=\&quot;hljs-number\&quot;>256</span>, num_beams=<span class=\&quot;hljs-number\&quot;>1</span>, **kwargs</span>):&quot;,&quot;        self.<span class=\&quot;hljs-built_in\&quot;>eval</span>()&quot;,&quot;        device = <span class=\&quot;hljs-built_in\&quot;>next</span>(self.parameters()).device&quot;,&quot;        input_values = input_values.to(device)&quot;,&quot;        &quot;,&quot;        encoder_outputs = self.encoder(input_values=input_values, attention_mask=attention_mask)&quot;,&quot;        hidden_states = encoder_outputs.last_hidden_state&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> attention_mask <span class=\&quot;hljs-keyword\&quot;>is</span> <span class=\&quot;hljs-keyword\&quot;>not</span> <span class=\&quot;hljs-literal\&quot;>None</span>:&quot;,&quot;            output_lengths = self.encoder._get_feat_extract_output_lengths(attention_mask.<span class=\&quot;hljs-built_in\&quot;>sum</span>(-<span class=\&quot;hljs-number\&quot;>1</span>))&quot;,&quot;            batch_size, max_length = hidden_states.shape[:<span class=\&quot;hljs-number\&quot;>2</span>]&quot;,&quot;            encoder_attention_mask = torch.zeros(&quot;,&quot;                (batch_size, max_length), dtype=torch.<span class=\&quot;hljs-built_in\&quot;>bool</span>, device=hidden_states.device&quot;,&quot;            )&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>for</span> i, length <span class=\&quot;hljs-keyword\&quot;>in</span> <span class=\&quot;hljs-built_in\&quot;>enumerate</span>(output_lengths):&quot;,&quot;                encoder_attention_mask[i, :length] = <span class=\&quot;hljs-literal\&quot;>True</span>&quot;,&quot;            encoder_padding_mask = ~encoder_attention_mask&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>else</span>:&quot;,&quot;            encoder_padding_mask = torch.zeros_like(hidden_states[..., <span class=\&quot;hljs-number\&quot;>0</span>], dtype=torch.<span class=\&quot;hljs-built_in\&quot;>bool</span>)&quot;,&quot;            encoder_attention_mask = torch.ones_like(hidden_states[..., <span class=\&quot;hljs-number\&quot;>0</span>], dtype=torch.<span class=\&quot;hljs-built_in\&quot;>bool</span>)&quot;,&quot;&quot;,&quot;        adapted_states = self.adapter(hidden_states, src_key_padding_mask=encoder_padding_mask)&quot;,&quot;        &quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> self.decoder.generate(&quot;,&quot;            encoder_outputs=BaseModelOutput(last_hidden_state=adapted_states),&quot;,&quot;            attention_mask=encoder_attention_mask,&quot;,&quot;            max_length=max_length,&quot;,&quot;            num_beams=num_beams,&quot;,&quot;            do_sample=<span class=\&quot;hljs-literal\&quot;>False</span>,&quot;,&quot;            no_repeat_ngram_size=<span class=\&quot;hljs-number\&quot;>2</span>,&quot;,&quot;            repetition_penalty=<span class=\&quot;hljs-number\&quot;>2.0</span>,&quot;,&quot;            **kwargs&quot;,&quot;        )&quot;],&quot;lineSelectorClass&quot;:&quot;blob-line&quot;,&quot;context&quot;:{&quot;repo&quot;:{&quot;name&quot;:&quot;huypd1508/wav2vec2-t5-Vietnamese&quot;,&quot;type&quot;:&quot;model&quot;},&quot;rev&quot;:&quot;main&quot;,&quot;path&quot;:&quot;modeling_wav2vec2_to_vit5_bottleneck.py&quot;,&quot;subpaths&quot;:[{&quot;dir&quot;:&quot;modeling_wav2vec2_to_vit5_bottleneck.py&quot;}]}}">


<div class="@container relative"><div class="@max-3xl:text-xs overflow-x-auto text-sm"><table class="min-w-full border-collapse font-mono"><tbody>
					<tr class="" id="L1">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="1">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> torch<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L2">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="2">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> torch.nn <span class="hljs-keyword">as</span> nn<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L3">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="3">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> transformers <span class="hljs-keyword">import</span> PreTrainedModel, Wav2Vec2Model, AutoModelForSeq2SeqLM<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L4">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="4">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> transformers.modeling_outputs <span class="hljs-keyword">import</span> BaseModelOutput<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L5">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="5">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> .configuration_wav2vec2_to_vit5_bottleneck <span class="hljs-keyword">import</span> Wav2Vec2ToVit5BottleneckConfig<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L6">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="6">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L7">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="7">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">class</span> <span class="hljs-title class_">BottleneckAdapter</span>(nn.Module):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L8">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="8">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">__init__</span>(<span class="hljs-params">self, input_dim, output_dim, num_layers=<span class="hljs-number">2</span>, num_heads=<span class="hljs-number">4</span>, bottleneck_dim=<span class="hljs-number">256</span></span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L9">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="9">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-built_in">super</span>().__init__()<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L10">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="10">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        encoder_layer = nn.TransformerEncoderLayer(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L11">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="11">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            d_model=bottleneck_dim,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L12">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="12">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            nhead=num_heads,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L13">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="13">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            dim_feedforward=<span class="hljs-number">1024</span>,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L14">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="14">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            dropout=<span class="hljs-number">0.1</span>,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L15">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="15">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            activation=<span class="hljs-string">&quot;gelu&quot;</span>,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L16">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="16">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            batch_first=<span class="hljs-literal">True</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L17">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="17">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L18">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="18">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L19">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="19">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.bottleneck_proj = nn.Linear(input_dim, bottleneck_dim)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L20">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="20">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.output_proj = nn.Linear(bottleneck_dim, output_dim)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L21">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="21">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L22">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="22">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">forward</span>(<span class="hljs-params">self, x, src_key_padding_mask=<span class="hljs-literal">None</span></span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L23">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="23">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Project to bottleneck</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L24">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="24">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        x = self.bottleneck_proj(x)      <!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L25">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="25">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        x = self.encoder(x, src_key_padding_mask=src_key_padding_mask)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L26">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="26">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        x = self.output_proj(x)          <!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L27">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="27">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> x<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L28">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="28">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L29">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="29">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">class</span> <span class="hljs-title class_">Wav2Vec2ToVit5WithAdapter</span>(<span class="hljs-title class_ inherited__">PreTrainedModel</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L30">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="30">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    config_class = Wav2Vec2ToVit5BottleneckConfig<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L31">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="31">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L32">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="32">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">__init__</span>(<span class="hljs-params">self, config</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L33">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="33">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-built_in">super</span>().__init__(config)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L34">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="34">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.encoder = Wav2Vec2Model.from_pretrained(config.encoder_model_name)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L35">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="35">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.decoder = AutoModelForSeq2SeqLM.from_pretrained(config.decoder_model_name)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L36">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="36">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.adapter = BottleneckAdapter(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L37">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="37">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            input_dim=self.encoder.config.hidden_size,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L38">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="38">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            output_dim=self.decoder.config.d_model,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L39">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="39">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            num_layers=config.num_layers,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L40">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="40">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            num_heads=config.num_heads,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L41">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="41">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            bottleneck_dim=config.bottleneck_dim<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L42">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="42">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L43">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="43">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L44">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="44">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">enable_input_require_grads</span>(<span class="hljs-params">self</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L45">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="45">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> <!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L46">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="46">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L47">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="47">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">get_input_embeddings</span>(<span class="hljs-params">self</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L48">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="48">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> self.decoder.get_input_embeddings()<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L49">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="49">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L50">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="50">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">set_input_embeddings</span>(<span class="hljs-params">self, value</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L51">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="51">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.decoder.set_input_embeddings(value)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L52">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="52">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L53">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="53">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">forward</span>(<span class="hljs-params">self, input_values=<span class="hljs-literal">None</span>, attention_mask=<span class="hljs-literal">None</span>, decoder_input_ids=<span class="hljs-literal">None</span>, labels=<span class="hljs-literal">None</span>, **kwargs</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L54">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="54">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        encoder_outputs = self.encoder(input_values=input_values, attention_mask=attention_mask)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L55">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="55">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        hidden_states = encoder_outputs.last_hidden_state   <span class="hljs-comment"># Get last hidden_state from encoder outputs</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L56">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="56">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L57">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="57">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> self.training:                      <span class="hljs-comment"># Fix for gradient checkpointing</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L58">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="58">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            hidden_states.requires_grad_(<span class="hljs-literal">True</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L59">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="59">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> hidden_states.grad_fn <span class="hljs-keyword">is</span> <span class="hljs-literal">None</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L60">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="60">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                hidden_states.retain_grad()<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L61">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="61">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L62">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="62">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L63">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="63">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> attention_mask <span class="hljs-keyword">is</span> <span class="hljs-keyword">not</span> <span class="hljs-literal">None</span>:        <span class="hljs-comment"># Get attention_mask that matched with last hidden_state size</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L64">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="64">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L65">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="65">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            output_lengths = self.encoder._get_feat_extract_output_lengths(attention_mask.<span class="hljs-built_in">sum</span>(-<span class="hljs-number">1</span>))<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L66">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="66">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L67">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="67">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            batch_size, max_length = hidden_states.shape[:<span class="hljs-number">2</span>]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L68">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="68">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            encoder_attention_mask = torch.zeros(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L69">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="69">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                (batch_size, max_length), dtype=torch.<span class="hljs-built_in">bool</span>, device=hidden_states.device<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L70">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="70">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L71">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="71">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">for</span> i, length <span class="hljs-keyword">in</span> <span class="hljs-built_in">enumerate</span>(output_lengths):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L72">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="72">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                encoder_attention_mask[i, :length] = <span class="hljs-literal">True</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L73">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="73">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            encoder_padding_mask = ~encoder_attention_mask  <!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L74">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="74">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">else</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L75">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="75">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            encoder_padding_mask = torch.zeros_like(hidden_states[..., <span class="hljs-number">0</span>], dtype=torch.<span class="hljs-built_in">bool</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L76">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="76">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            encoder_attention_mask = torch.ones_like(hidden_states[..., <span class="hljs-number">0</span>], dtype=torch.<span class="hljs-built_in">bool</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L77">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="77">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L78">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="78">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        adapted_states = self.adapter(hidden_states, src_key_padding_mask=encoder_padding_mask) <span class="hljs-comment"># Adapter Output</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L79">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="79">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Here we call the T5 model, but only use the decoder by passing adapter output to encoder_outputs</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L80">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="80">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        outputs = self.decoder(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L81">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="81">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            encoder_outputs=BaseModelOutput(last_hidden_state=adapted_states),<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L82">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="82">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            attention_mask=encoder_attention_mask,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L83">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="83">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            decoder_input_ids=decoder_input_ids,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L84">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="84">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            labels=labels,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L85">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="85">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            return_dict=<span class="hljs-literal">True</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L86">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="86">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L87">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="87">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L88">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="88">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> {<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L89">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="89">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-string">&quot;loss&quot;</span>: outputs.loss.unsqueeze(<span class="hljs-number">0</span>) <span class="hljs-keyword">if</span> outputs.loss <span class="hljs-keyword">is</span> <span class="hljs-keyword">not</span> <span class="hljs-literal">None</span> <span class="hljs-keyword">else</span> <span class="hljs-literal">None</span>,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L90">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="90">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-string">&quot;logits&quot;</span>: outputs.logits<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L91">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="91">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        }<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L92">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="92">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L93">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="93">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">generate</span>(<span class="hljs-params">self, input_values=<span class="hljs-literal">None</span>, attention_mask=<span class="hljs-literal">None</span>, max_length=<span class="hljs-number">256</span>, num_beams=<span class="hljs-number">1</span>, **kwargs</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L94">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="94">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.<span class="hljs-built_in">eval</span>()<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L95">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="95">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        device = <span class="hljs-built_in">next</span>(self.parameters()).device<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L96">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="96">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        input_values = input_values.to(device)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L97">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="97">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L98">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="98">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        encoder_outputs = self.encoder(input_values=input_values, attention_mask=attention_mask)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L99">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="99">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        hidden_states = encoder_outputs.last_hidden_state<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L100">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="100">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> attention_mask <span class="hljs-keyword">is</span> <span class="hljs-keyword">not</span> <span class="hljs-literal">None</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L101">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="101">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            output_lengths = self.encoder._get_feat_extract_output_lengths(attention_mask.<span class="hljs-built_in">sum</span>(-<span class="hljs-number">1</span>))<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L102">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="102">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            batch_size, max_length = hidden_states.shape[:<span class="hljs-number">2</span>]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L103">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="103">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            encoder_attention_mask = torch.zeros(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L104">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="104">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                (batch_size, max_length), dtype=torch.<span class="hljs-built_in">bool</span>, device=hidden_states.device<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L105">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="105">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L106">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="106">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">for</span> i, length <span class="hljs-keyword">in</span> <span class="hljs-built_in">enumerate</span>(output_lengths):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L107">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="107">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                encoder_attention_mask[i, :length] = <span class="hljs-literal">True</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L108">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="108">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            encoder_padding_mask = ~encoder_attention_mask<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L109">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="109">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">else</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L110">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="110">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            encoder_padding_mask = torch.zeros_like(hidden_states[..., <span class="hljs-number">0</span>], dtype=torch.<span class="hljs-built_in">bool</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L111">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="111">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            encoder_attention_mask = torch.ones_like(hidden_states[..., <span class="hljs-number">0</span>], dtype=torch.<span class="hljs-built_in">bool</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L112">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="112">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L113">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="113">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        adapted_states = self.adapter(hidden_states, src_key_padding_mask=encoder_padding_mask)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L114">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="114">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L115">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="115">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> self.decoder.generate(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L116">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="116">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            encoder_outputs=BaseModelOutput(last_hidden_state=adapted_states),<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L117">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="117">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            attention_mask=encoder_attention_mask,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L118">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="118">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            max_length=max_length,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L119">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="119">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            num_beams=num_beams,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L120">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="120">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            do_sample=<span class="hljs-literal">False</span>,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L121">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="121">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            no_repeat_ngram_size=<span class="hljs-number">2</span>,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L122">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="122">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            repetition_penalty=<span class="hljs-number">2.0</span>,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L123">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="123">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            **kwargs<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L124">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="124">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        )<!-- HTML_TAG_END --></td>
					</tr></tbody></table></div>
	</div></div></div>
				</div></section></div></main>

	</div>
		<script>
			 import("\/front\/build\/kube-4bcc544\/index.js"); window.moonSha = "kube-4bcc544\/"; window.__hf_deferred =
			{};
		</script>
		<!-- Stripe -->
		<script>
			if (["hf.co", "huggingface.co"].includes(window.location.hostname)) {
				const script = document.createElement("script");
				script.src = "https://js.stripe.com/v3/";
				script.async = true;
				document.head.appendChild(script);
			}
		</script>
	</body>
</html>
