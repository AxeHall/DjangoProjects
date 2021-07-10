from django.shortcuts import render
from django.views.generic import View


class MainView(View):
    def get(self, request):
<<<<<<< HEAD
        return render(request, template_name="main/wrapper.html")
    
class AboutView(View):
    def get(self, request):
        info_dashboard = [
            {"card_title": 125, "card_text": "Active Projects"},
            {"card_title": 200, "card_text": "Business Growth"},
            {"card_title": 530, "card_text": "Completed Projects"},
            {"card_title": 941, "card_text": "Happy Clients"},
        ]
        personals_info = [
            {"img_path": "images/customer1.jpg", "name": "Lisa Gally", "position":"Project Manager", "card_text": "Top Project Manager, 4 years of commercial development experience"},
            {"img_path": "images/customer2.jpg", "name": "Missy Limana", "position":"Python Developer", "card_text": "Python back-end developer with over 3 years of experience"},
            {"img_path": "images/customer3.jpg", "name": "Aana Brown", "position":"Full Stack Developer", "card_text": "Full Stack Developer with over 3 years of experience"},
            {"img_path": "images/customer3.jpg", "name": "Aana Brown", "position":"Technical Director", "card_text": "Experienced Technology Executive with a demonstrated history of working in the Telecom Industry and IT."},
        ]
        business_process = [
            {"img_path": "images/quality-results.png", "media_title": "Quality Results", "media_description": " Projects and programmes are regularly reviewed to assess their quality, effectiveness and cost-effectiveness. This enables us to learn from our experiences, ensure effective project management and achieve sustainable results."},
            {"img_path": "images/analytics.png", "media_title": "Analytics", "media_description": "We support you in your individual analysis of your requirements. Depending on the industry and the size as well as the complexity of your communication infrastructures, your software solution will vary."},
            {"img_path": "images/affordable-pricing.png", "media_title": "Affordable Pricing", "media_description": "Having a balanced range of energy sources will help avoid over-reliance on too few sources, and help ensure that energy prices are affordable for consumers and businesses alike."},
            {"img_path": "images/easy-to-use.png", "media_title": "Easy To Use", "media_description": "Above all, ease of use is critical to creating happy customers in the longer term. If your product, service, software or application is super simple to use, not only will people love it, but they’ll keep coming back."},
            {"img_path": "images/free-support.png", "media_title": "Free Support", "media_description": "We support you in your daily use of SOLUTION and in solving specific issues related to it. These might include database migrations, process modeling and adaptions, as well as integration of interfaces."},
            {"img_path": "images/effectively-increase.png", "media_title": "Analytics", "media_description": "You don’t need to go to IT to create your own documents and spreadsheets. Why should processes be any different? Take charge of your processes, design your own forms and workflows, and bring automated efficiency to your team."},
        ]
        return render(request, template_name="main/about.html", context={"info_dashboard_data": info_dashboard, "personal": personals_info, "business_process": business_process})

class HomeView(View):
    def get(self, request):
        body_data = [
            {
            "home_image_path": "images/learn-img.jpg",
            "home_title": "We are a Creative Digital Agency & Marketing Experts",
            "home_theme": "Pure Workflow. No Limits. Boundless configuration with best performance, more process control & resource savings",
            "home_description": "You don’t need to go to IT to create your own documents and spreadsheets. Why should processes be any different? Take charge of your processes, design your own forms and workflows, and bring automated efficiency to your team."
            }
        ]
        return render(request, template_name="main/home.html", 
        context={"home_data": body_data})

class NewsView(View):
    def get(self, request):
        news_data = [
            {"img_path": "images/news1.jpg", "card_title": "5G, IoT, SaaS to drive Netherlands data centre growth", "card_text": "Government initiatives and enterprise deployment of IoT, 5G, SaaS, and AI applications will fuel an increase in data centre investment."},
            {"img_path": "images/news2.jpg", "card_title": "Microsoft's plan to remake Windows — what that might mean", "card_text": "In two weeks, Microsoft, plans to unveil the 'next generation' of Windows. But isn't Windows 10 supposed to be the last generation of the ubiquitous OS?"},
            {"img_path": "images/news3.jpg", "card_title": "Noteworthy technology acquisitions 2021", "card_text": "Global tech merger-and-acquisition deals totaled $634.1 billion in 2020, an increase of 91.8% year-on-year. Can 2021 match that for blockbuster activity?"},
            {"img_path": "images/news1.jpg", "card_title": "A Clubhouse for the office? Slack unveils ‘Huddles’ audio chat rooms", "card_text": "Slack hopes to replicate ad-hoc workplace chats for remote workers with a “lightweight, audio-first” communication tool."},
            {"img_path": "images/news2.jpg", "card_title": "WSJ leaks Apple’s digital healthcare plan", "card_text": "Apple has been working to develop its own subscription-based healthcare service, but the effort may have stalled, report claims."},
            {"img_path": "images/news3.jpg", "card_title": "Securing the Apple mobile enterprise takes context", "card_text": "Truce Software CEO Joe Boyle talks about Apple's place in business and the evolution of new security models for the remote enterprise."},
        ]
        return render(request, template_name="main/news.html", context={"news_data": news_data})

class ServicesView(View):
    def get(self, request):
        right_top_content = [
            {"img_path": "images/web-design.png", "card_title": "Web Design", "card_text": "Manage a stably working website with quick access to all information."},
            {"img_path": "images/marketing.png", "card_title": "Marketing", 'card_text': "Our specialists will audit the site and, based on the results."},
        ]

        right_lower_content = [
            {"img_path": "images/seo.png", "card_title": "SEO", 'card_text': "Improve website performance with comprehensive search engine optimization."},
            {"img_path": "images/graphics-design.png", "card_title": "Graphics Design", 'card_text': "Connect interactive maps, feedback form, widgets, etc."},
        ]
        return render(request, template_name="main/services.html", context={"right_top_content": right_top_content, "right_lower_content": right_lower_content})


=======
        return render(
            request,
            template_name="main/home.html",
        )

    def post(self, request):
        pass
>>>>>>> upstream/main
