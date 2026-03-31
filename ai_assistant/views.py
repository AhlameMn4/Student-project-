from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from accounts.models import UserRole

from .models import AIConversation, AIMessage, AIQueryLog
from .services import build_guided_answer


@login_required
def assistant_page(request):
    if request.user.role != UserRole.STUDENT or not hasattr(request.user, "student_profile"):
        return JsonResponse({"detail": "AI assistant is available for students only."}, status=403)

    answer = ""
    query = ""
    if request.method == "POST":
        query = request.POST.get("query", "").strip()
        if query:
            student_profile = request.user.student_profile
            started = timezone.now()
            intent, answer, references = build_guided_answer(student_profile, query)
            elapsed = int((timezone.now() - started).total_seconds() * 1000)

            conversation, _ = AIConversation.objects.get_or_create(
                student=student_profile, title="Academic Assistant"
            )
            AIMessage.objects.create(conversation=conversation, role="user", content=query)
            AIMessage.objects.create(
                conversation=conversation,
                role="assistant",
                content=answer,
                references_json=references,
            )
            AIQueryLog.objects.create(
                student=student_profile,
                query=query,
                intent=intent,
                response_time_ms=elapsed,
                tokens_in=0,
                tokens_out=0,
                status="ok",
            )

    return render(request, "ai_assistant/assistant.html", {"answer": answer, "query": query})
